"""Base classes for validation framework."""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime


class ValidationLevel(str, Enum):
    """Severity levels for validation results."""
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    SUCCESS = "success"


class ValidationResult(BaseModel):
    """Result from a single validation check."""
    
    level: ValidationLevel
    message: str
    path: str
    validator_name: str
    original_value: Optional[Any] = None
    repaired_value: Optional[Any] = None
    was_repaired: bool = False
    metadata: Dict[str, Any] = Field(default_factory=dict)
    
    class Config:
        arbitrary_types_allowed = True


class ValidationReport(BaseModel):
    """
    Complete validation report with summary statistics.
    
    Examples:
        >>> report = ValidationReport()
        >>> result = ValidationResult(
        ...     level=ValidationLevel.ERROR,
        ...     message="Invalid term",
        ...     path="terms[0].id",
        ...     validator_name="TermValidator"
        ... )
        >>> report.add_result(result)
        >>> report.total_checks
        1
        >>> len(report.errors)
        1
        >>> report.errors[0].message
        'Invalid term'
    """
    
    results: List[ValidationResult] = Field(default_factory=list)
    start_time: datetime = Field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    file_path: Optional[str] = None
    
    @property
    def total_checks(self) -> int:
        """
        Total number of validation checks performed.
        
        >>> report = ValidationReport()
        >>> report.total_checks
        0
        >>> report.add_result(ValidationResult(
        ...     level=ValidationLevel.INFO,
        ...     message="test",
        ...     path="test",
        ...     validator_name="test"
        ... ))
        >>> report.total_checks
        1
        """
        return len(self.results)
    
    @property
    def errors(self) -> List[ValidationResult]:
        """Get all error-level results."""
        return [r for r in self.results if r.level == ValidationLevel.ERROR]
    
    @property
    def warnings(self) -> List[ValidationResult]:
        """Get all warning-level results."""
        return [r for r in self.results if r.level == ValidationLevel.WARNING]
    
    @property
    def repairs_made(self) -> List[ValidationResult]:
        """Get all results where repairs were made."""
        return [r for r in self.results if r.was_repaired]
    
    @property
    def success_count(self) -> int:
        """Count of successful validations."""
        return len([r for r in self.results if r.level == ValidationLevel.SUCCESS])
    
    def add_result(self, result: ValidationResult) -> None:
        """Add a validation result to the report."""
        self.results.append(result)
    
    def finalize(self) -> None:
        """Mark the report as complete."""
        self.end_time = datetime.now()
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get summary statistics for the report.
        
        Returns:
            Dictionary with summary statistics
            
        Examples:
            >>> report = ValidationReport()
            >>> report.add_result(ValidationResult(
            ...     level=ValidationLevel.ERROR,
            ...     message="Test error",
            ...     path="test.path",
            ...     validator_name="TestValidator"
            ... ))
            >>> summary = report.get_summary()
            >>> summary["errors"]
            1
            >>> summary["total_checks"]
            1
            >>> "duration_seconds" in summary
            True
        """
        return {
            "total_checks": self.total_checks,
            "errors": len(self.errors),
            "warnings": len(self.warnings),
            "success": self.success_count,
            "repairs_made": len(self.repairs_made),
            "duration_seconds": (
                (self.end_time - self.start_time).total_seconds()
                if self.end_time else None
            ),
            "file_path": self.file_path
        }
    
    def to_tsv_rows(self) -> List[Dict[str, Any]]:
        """Convert results to rows suitable for TSV output."""
        rows = []
        for result in self.results:
            rows.append({
                "path": result.path,
                "level": result.level.value,
                "validator": result.validator_name,
                "message": result.message,
                "original_value": str(result.original_value) if result.original_value else "",
                "repaired_value": str(result.repaired_value) if result.repaired_value else "",
                "was_repaired": "yes" if result.was_repaired else "no"
            })
        return rows
    
    def get_errors_by_path(self) -> Dict[str, List[ValidationResult]]:
        """Group errors by their path for easier debugging."""
        errors_by_path: Dict[str, List[ValidationResult]] = {}
        for error in self.errors:
            if error.path not in errors_by_path:
                errors_by_path[error.path] = []
            errors_by_path[error.path].append(error)
        return errors_by_path


class Validator(ABC):
    """Abstract base class for validators."""
    
    def __init__(self, name: Optional[str] = None):
        """Initialize validator with optional name."""
        self.name = name or self.__class__.__name__
    
    @abstractmethod
    def validate(
        self,
        value: Any,
        path: str,
        context: Optional[Dict[str, Any]] = None,
        repair: bool = False
    ) -> Union[ValidationResult, List[ValidationResult]]:
        """
        Validate a value and optionally repair it.
        
        Args:
            value: The value to validate
            path: The path to this value in the data structure
            context: Optional context from parent/sibling nodes
            repair: Whether to attempt repairs
            
        Returns:
            ValidationResult or list of ValidationResults
        """
        pass
    
    def applies_to(self, value: Any, path: str) -> bool:
        """
        Check if this validator applies to the given value.
        
        Override this method to control when the validator runs.
        By default, returns True (validates everything).
        
        Args:
            value: The value to check
            path: The path to this value
            
        Returns:
            True if this validator should run on this value
            
        Examples:
            >>> class StringValidator(Validator):
            ...     def applies_to(self, value: Any, path: str) -> bool:
            ...         return isinstance(value, str)
            ...     def validate(self, value: Any, path: str, context=None, repair=False):
            ...         return self._create_result(
            ...             ValidationLevel.SUCCESS,
            ...             "Valid string",
            ...             path
            ...         )
            
            >>> validator = StringValidator()
            >>> validator.applies_to("test", "field")
            True
            >>> validator.applies_to(123, "field")
            False
            >>> validator.applies_to({"key": "value"}, "field")
            False
        """
        return True
    
    def _create_result(
        self,
        level: ValidationLevel,
        message: str,
        path: str,
        original_value: Optional[Any] = None,
        repaired_value: Optional[Any] = None,
        was_repaired: bool = False,
        metadata: Optional[Dict[str, Any]] = None
    ) -> ValidationResult:
        """Helper method to create a ValidationResult."""
        return ValidationResult(
            level=level,
            message=message,
            path=path,
            validator_name=self.name,
            original_value=original_value,
            repaired_value=repaired_value,
            was_repaired=was_repaired,
            metadata=metadata or {}
        )