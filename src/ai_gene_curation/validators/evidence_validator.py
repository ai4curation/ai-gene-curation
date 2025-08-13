"""Validator for evidence and publication references."""

import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Set
from .base import Validator, ValidationResult, ValidationLevel


class EvidenceValidator(Validator):
    """
    Validates evidence objects including references, titles, and evidence codes.
    
    Examples:
        >>> validator = EvidenceValidator(check_titles=False)
        >>> evidence = {
        ...     "reference": "PMID:12345678",
        ...     "title": "Test paper",
        ...     "evidence_type": "IDA"
        ... }
        >>> results = validator._validate_evidence(evidence, "test.evidence", False)
        >>> len(results)
        1
        >>> results[0].level.value
        'success'
        
        >>> # Test invalid evidence code
        >>> evidence = {"reference": "PMID:123", "evidence_type": "INVALID"}
        >>> results = validator._validate_evidence(evidence, "test", False)
        >>> any(r.level == ValidationLevel.ERROR for r in results)
        True
    """
    
    # Valid GO evidence codes
    VALID_EVIDENCE_CODES = {
        "EXP": "Inferred from Experiment",
        "IDA": "Inferred from Direct Assay",
        "IPI": "Inferred from Physical Interaction",
        "IMP": "Inferred from Mutant Phenotype",
        "IGI": "Inferred from Genetic Interaction",
        "IEP": "Inferred from Expression Pattern",
        "ISS": "Inferred from Sequence or structural Similarity",
        "ISO": "Inferred from Sequence Orthology",
        "ISA": "Inferred from Sequence Alignment",
        "ISM": "Inferred from Sequence Model",
        "IGC": "Inferred from Genomic Context",
        "IBA": "Inferred from Biological aspect of Ancestor",
        "IBD": "Inferred from Biological aspect of Descendant",
        "IKR": "Inferred from Key Residues",
        "IRD": "Inferred from Rapid Divergence",
        "RCA": "Inferred from Reviewed Computational Analysis",
        "TAS": "Traceable Author Statement",
        "NAS": "Non-traceable Author Statement",
        "IC": "Inferred by Curator",
        "ND": "No biological Data available",
        "IEA": "Inferred from Electronic Annotation",
        "HTP": "High Throughput",
        "HDA": "High Throughput Direct Assay",
        "HMP": "High Throughput Mutant Phenotype",
        "HGI": "High Throughput Genetic Interaction",
        "HEP": "High Throughput Expression Pattern"
    }
    
    def __init__(
        self,
        name: Optional[str] = None,
        publications_dir: Optional[Path] = None,
        check_titles: bool = True,
        check_evidence_codes: bool = True,
        use_pubmed_api: bool = False,
        cache_dir: Optional[Path] = None
    ):
        """
        Initialize the evidence validator.
        
        Args:
            name: Optional name for the validator
            publications_dir: Directory containing cached publication files
            check_titles: Whether to validate publication titles
            check_evidence_codes: Whether to validate GO evidence codes
            use_pubmed_api: Whether to fetch from PubMed API if not cached
            cache_dir: Directory for caching fetched data
        """
        super().__init__(name or "EvidenceValidator")
        self.publications_dir = publications_dir or Path("publications")
        self.check_titles = check_titles
        self.check_evidence_codes = check_evidence_codes
        self.use_pubmed_api = use_pubmed_api
        self.cache_dir = cache_dir or Path.home() / ".cache" / "ai_gene_curation"
        self._title_cache: Dict[str, Optional[str]] = {}
        self._api_call_count = 0
        self._last_api_call = 0.0
    
    def applies_to(self, value: Any, path: str) -> bool:
        """Check if this validator applies to the value."""
        # Check if this looks like an evidence/support object
        if isinstance(value, dict):
            # Evidence objects have 'reference' field
            # Support objects are lists containing evidence objects
            return "reference" in value or path.endswith(".support")
        elif isinstance(value, list) and path.endswith(".support"):
            # Support is a list of evidence objects
            return True
        return False
    
    def validate(
        self,
        value: Any,
        path: str,
        context: Optional[Dict[str, Any]] = None,
        repair: bool = False
    ) -> List[ValidationResult]:
        """Validate evidence or support objects."""
        results = []
        
        # Handle list of support objects
        if isinstance(value, list) and path.endswith(".support"):
            for i, item in enumerate(value):
                item_path = f"{path}[{i}]"
                if isinstance(item, dict) and "reference" in item:
                    results.extend(self._validate_evidence(item, item_path, repair))
            return results
        
        # Handle single evidence object
        if isinstance(value, dict) and "reference" in value:
            results.extend(self._validate_evidence(value, path, repair))
        
        return results
    
    def _validate_evidence(self, evidence: Dict[str, Any], path: str, repair: bool) -> List[ValidationResult]:
        """Validate a single evidence object."""
        results = []
        
        reference = evidence.get("reference", "")
        title = evidence.get("title")
        evidence_type = evidence.get("evidence_type")
        
        # Validate reference format
        if not reference:
            results.append(self._create_result(
                ValidationLevel.ERROR,
                "Evidence missing 'reference' field",
                path,
                original_value=evidence
            ))
            return results
        
        # Check reference format
        if reference.startswith("PMID:"):
            pmid = reference[5:]
            if not pmid.isdigit():
                results.append(self._create_result(
                    ValidationLevel.ERROR,
                    f"Invalid PMID format: {reference}",
                    f"{path}.reference",
                    original_value=reference
                ))
            elif self.check_titles:
                # Validate title against PubMed
                correct_title = self._get_publication_title(pmid)
                if correct_title:
                    if title and title != correct_title:
                        if repair:
                            evidence["title"] = correct_title
                            results.append(self._create_result(
                                ValidationLevel.WARNING,
                                f"Fixed title for {reference}",
                                f"{path}.title",
                                original_value=title,
                                repaired_value=correct_title,
                                was_repaired=True
                            ))
                        else:
                            results.append(self._create_result(
                                ValidationLevel.ERROR,
                                f"Title mismatch for {reference}",
                                f"{path}.title",
                                original_value=title,
                                metadata={"correct_title": correct_title}
                            ))
                    elif not title:
                        if repair:
                            evidence["title"] = correct_title
                            results.append(self._create_result(
                                ValidationLevel.INFO,
                                f"Added missing title for {reference}",
                                f"{path}.title",
                                repaired_value=correct_title,
                                was_repaired=True
                            ))
                        else:
                            results.append(self._create_result(
                                ValidationLevel.WARNING,
                                f"Missing title for {reference}",
                                f"{path}.title",
                                metadata={"suggested_title": correct_title}
                            ))
        elif reference.startswith("GO_REF:"):
            # GO reference - could validate format
            go_ref = reference[7:]
            if not go_ref.isdigit() or len(go_ref) != 7:
                results.append(self._create_result(
                    ValidationLevel.WARNING,
                    f"Unusual GO_REF format: {reference}",
                    f"{path}.reference",
                    original_value=reference
                ))
        else:
            # Unknown reference format
            results.append(self._create_result(
                ValidationLevel.WARNING,
                f"Unknown reference format: {reference}",
                f"{path}.reference",
                original_value=reference
            ))
        
        # Validate evidence code
        if self.check_evidence_codes and evidence_type:
            if evidence_type not in self.VALID_EVIDENCE_CODES:
                # Try case-insensitive match
                upper_type = evidence_type.upper()
                if upper_type in self.VALID_EVIDENCE_CODES:
                    if repair:
                        evidence["evidence_type"] = upper_type
                        results.append(self._create_result(
                            ValidationLevel.INFO,
                            f"Fixed evidence code case: {evidence_type} -> {upper_type}",
                            f"{path}.evidence_type",
                            original_value=evidence_type,
                            repaired_value=upper_type,
                            was_repaired=True
                        ))
                    else:
                        results.append(self._create_result(
                            ValidationLevel.WARNING,
                            f"Evidence code has incorrect case: {evidence_type} (should be {upper_type})",
                            f"{path}.evidence_type",
                            original_value=evidence_type
                        ))
                else:
                    results.append(self._create_result(
                        ValidationLevel.ERROR,
                        f"Invalid evidence code: {evidence_type}",
                        f"{path}.evidence_type",
                        original_value=evidence_type,
                        metadata={"valid_codes": list(self.VALID_EVIDENCE_CODES.keys())}
                    ))
        elif self.check_evidence_codes and not evidence_type:
            results.append(self._create_result(
                ValidationLevel.WARNING,
                "Missing evidence_type field",
                f"{path}.evidence_type"
            ))
        
        # If no issues found, report success
        if not results:
            results.append(self._create_result(
                ValidationLevel.SUCCESS,
                f"Evidence {reference} validated successfully",
                path,
                original_value=evidence
            ))
        
        return results
    
    def _get_publication_title(self, pmid: str) -> Optional[str]:
        """Get publication title from cache or API."""
        if pmid in self._title_cache:
            return self._title_cache[pmid]
        
        # Check filesystem cache first
        cache_file = self.publications_dir / f"PMID_{pmid}.md"
        if cache_file.exists():
            try:
                content = cache_file.read_text()
                # Parse frontmatter to get title
                if content.startswith('---'):
                    lines = content.split('\n')
                    for line in lines[1:]:
                        if line.startswith('---'):
                            break
                        if line.startswith('title:'):
                            title = line[6:].strip()
                            # Remove quotes if present
                            if title.startswith('"') and title.endswith('"'):
                                title = title[1:-1]
                            elif title.startswith("'") and title.endswith("'"):
                                title = title[1:-1]
                            self._title_cache[pmid] = title
                            return title
            except Exception:
                pass
        
        # Fetch from PubMed API if enabled
        if self.use_pubmed_api:
            title = self._fetch_from_pubmed(pmid)
            self._title_cache[pmid] = title
            return title
        
        self._title_cache[pmid] = None
        return None
    
    def _fetch_from_pubmed(self, pmid: str) -> Optional[str]:
        """Fetch title from PubMed API with rate limiting."""
        try:
            # Rate limit to 3 requests per second
            current_time = time.time()
            if current_time - self._last_api_call < 0.35:
                time.sleep(0.35 - (current_time - self._last_api_call))
            
            from Bio import Entrez
            Entrez.email = "ai-gene-curation@example.com"
            
            handle = Entrez.esummary(db="pubmed", id=pmid, retmode="xml")
            records = Entrez.read(handle)
            handle.close()
            
            self._last_api_call = time.time()
            self._api_call_count += 1
            
            if records and not records[0].get('error'):
                title = str(records[0].get('Title', '')).rstrip('.')
                return title
        except Exception:
            pass
        
        return None