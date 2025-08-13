"""Validator for ontology terms."""

import re
from typing import Any, Dict, List, Optional, Set, Union
from pathlib import Path
import yaml
from .base import Validator, ValidationResult, ValidationLevel


class TermValidator(Validator):
    """Validates ontology terms against configured ontologies."""
    
    # Default ontologies to check
    DEFAULT_ONTOLOGIES = {
        "GO": "Gene Ontology",
        "HP": "Human Phenotype Ontology", 
        "MONDO": "Mondo Disease Ontology",
        "CL": "Cell Ontology",
        "UBERON": "Uberon Anatomy Ontology",
        "CHEBI": "Chemical Entities of Biological Interest",
        "PR": "Protein Ontology",
        "SO": "Sequence Ontology",
        "PATO": "Phenotype And Trait Ontology"
    }
    
    def __init__(
        self,
        name: Optional[str] = None,
        ontologies: Optional[Dict[str, str]] = None,
        check_obsolete: bool = True,
        check_labels: bool = True,
        oak_adapters: Optional[Dict[str, Any]] = None,
        cache_dir: Optional[Path] = None
    ):
        """
        Initialize the term validator.
        
        Args:
            name: Optional name for the validator
            ontologies: Dict of ontology prefixes to check (default: DEFAULT_ONTOLOGIES)
            check_obsolete: Whether to check for obsolete terms
            check_labels: Whether to validate term labels match
            oak_adapters: Optional pre-loaded OAK adapters
            cache_dir: Directory for caching ontology data
        """
        super().__init__(name or "TermValidator")
        self.ontologies = ontologies or self.DEFAULT_ONTOLOGIES
        self.check_obsolete = check_obsolete
        self.check_labels = check_labels
        self.oak_adapters = oak_adapters or {}
        self.cache_dir = cache_dir or Path.home() / ".cache" / "ai_gene_curation"
        self._label_cache: Dict[str, str] = {}
        self._obsolete_cache: Dict[str, Optional[str]] = {}
    
    def applies_to(self, value: Any, path: str) -> bool:
        """Check if this validator applies to the value."""
        # Check if this looks like a term object
        if isinstance(value, dict):
            return "id" in value and "label" in value and self._is_ontology_term(value.get("id"))
        return False
    
    def validate(
        self,
        value: Any,
        path: str,
        context: Optional[Dict[str, Any]] = None,
        repair: bool = False
    ) -> List[ValidationResult]:
        """Validate an ontology term."""
        results: List[ValidationResult] = []
        
        if not isinstance(value, dict):
            return results
        
        term_id = value.get("id")
        term_label = value.get("label")
        
        if not term_id:
            results.append(self._create_result(
                ValidationLevel.ERROR,
                "Term missing 'id' field",
                path,
                original_value=value
            ))
            return results
        
        # Check ID format
        if not self._is_valid_term_format(term_id):
            results.append(self._create_result(
                ValidationLevel.ERROR,
                f"Invalid term ID format: {term_id}",
                f"{path}.id",
                original_value=term_id
            ))
            return results
        
        # Check if term exists and get correct label
        correct_label = self._get_term_label(term_id)
        
        if correct_label is None:
            results.append(self._create_result(
                ValidationLevel.WARNING,
                f"Could not verify term {term_id} (may not exist or network error)",
                f"{path}.id",
                original_value=term_id
            ))
        elif self.check_labels and term_label and term_label != correct_label:
            # Label mismatch
            if repair:
                value["label"] = correct_label
                results.append(self._create_result(
                    ValidationLevel.WARNING,
                    f"Fixed label mismatch for {term_id}: '{term_label}' -> '{correct_label}'",
                    f"{path}.label",
                    original_value=term_label,
                    repaired_value=correct_label,
                    was_repaired=True
                ))
            else:
                results.append(self._create_result(
                    ValidationLevel.ERROR,
                    f"Label mismatch for {term_id}: got '{term_label}', expected '{correct_label}'",
                    f"{path}.label",
                    original_value=term_label,
                    metadata={"correct_label": correct_label}
                ))
        
        # Check for obsolete terms
        if self.check_obsolete:
            replacement = self._get_obsolete_replacement(term_id)
            if replacement:
                if repair and replacement != "NO_REPLACEMENT":
                    # Parse replacement ID and get its label
                    replacement_label = self._get_term_label(replacement)
                    if replacement_label:
                        value["id"] = replacement
                        value["label"] = replacement_label
                        results.append(self._create_result(
                            ValidationLevel.WARNING,
                            f"Replaced obsolete term {term_id} with {replacement}",
                            path,
                            original_value={"id": term_id, "label": term_label},
                            repaired_value={"id": replacement, "label": replacement_label},
                            was_repaired=True
                        ))
                else:
                    msg = f"Term {term_id} is obsolete"
                    if replacement != "NO_REPLACEMENT":
                        msg += f" (suggested replacement: {replacement})"
                    results.append(self._create_result(
                        ValidationLevel.WARNING,
                        msg,
                        f"{path}.id",
                        original_value=term_id,
                        metadata={"replacement": replacement if replacement != "NO_REPLACEMENT" else None}
                    ))
        
        # If no issues found, report success
        if not results:
            results.append(self._create_result(
                ValidationLevel.SUCCESS,
                f"Term {term_id} validated successfully",
                path,
                original_value=value
            ))
        
        return results
    
    def _is_ontology_term(self, value: Any) -> bool:
        """
        Check if value looks like an ontology term ID.
        
        Examples:
            >>> validator = TermValidator()
            >>> validator._is_ontology_term("GO:0001234")
            True
            >>> validator._is_ontology_term("HP:0000001")
            True
            >>> validator._is_ontology_term("MONDO_0000001")
            True
            >>> validator._is_ontology_term("not_a_term")
            False
            >>> validator._is_ontology_term(123)
            False
        """
        if not isinstance(value, str):
            return False
        # Check for standard ontology ID patterns
        return bool(re.match(r'^[A-Z]+[_:]?\d+$', value))
    
    def _is_valid_term_format(self, term_id: str) -> bool:
        """Check if term ID has valid format."""
        # Check against known ontology prefixes
        for prefix in self.ontologies:
            if term_id.startswith(f"{prefix}:") or term_id.startswith(f"{prefix}_"):
                return True
        return False
    
    def _get_term_label(self, term_id: str) -> Optional[str]:
        """Get the correct label for a term from OAK/cache."""
        if term_id in self._label_cache:
            return self._label_cache[term_id]
        
        # Try to get from OAK adapter
        prefix = term_id.split(":")[0] if ":" in term_id else term_id.split("_")[0]
        
        if prefix in self.oak_adapters:
            try:
                adapter = self.oak_adapters[prefix]
                label = adapter.label(term_id)
                self._label_cache[term_id] = label
                return label
            except Exception:
                pass
        
        # Could also check a cached file or make API call here
        return None
    
    def _get_obsolete_replacement(self, term_id: str) -> Optional[str]:
        """Check if term is obsolete and get replacement if available."""
        if term_id in self._obsolete_cache:
            return self._obsolete_cache[term_id]
        
        # Try to get from OAK adapter
        prefix = term_id.split(":")[0] if ":" in term_id else term_id.split("_")[0]
        
        if prefix in self.oak_adapters:
            try:
                adapter = self.oak_adapters[prefix]
                # Check if obsolete
                if adapter.is_obsolete(term_id):
                    # Try to get replacement
                    replacements = adapter.get_replaced_by(term_id)
                    if replacements:
                        replacement = replacements[0]
                        self._obsolete_cache[term_id] = replacement
                        return replacement
                    else:
                        self._obsolete_cache[term_id] = "NO_REPLACEMENT"
                        return "NO_REPLACEMENT"
            except Exception:
                pass
        
        self._obsolete_cache[term_id] = None
        return None