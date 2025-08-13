"""Test validators for demonstration and testing purposes."""

from typing import Any, Dict, List, Optional, Union
from .base import Validator, ValidationResult, ValidationLevel


class RangeValidator(Validator):
    """
    Validates that numeric values are within a specified range.
    
    Examples:
        >>> validator = RangeValidator(min_value=0, max_value=100)
        >>> result = validator.validate(50, "score", repair=False)
        >>> result.level
        <ValidationLevel.SUCCESS: 'success'>
        
        >>> result = validator.validate(150, "score", repair=False)
        >>> result.level
        <ValidationLevel.ERROR: 'error'>
        >>> result.message
        'Value 150 is out of range [0, 100]'
        
        >>> # Test with repair
        >>> result = validator.validate(150, "score", repair=True)
        >>> result.was_repaired
        True
        >>> result.repaired_value
        100
    """
    
    def __init__(
        self,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None,
        paths: Optional[List[str]] = None,
        name: Optional[str] = None
    ):
        """
        Initialize the range validator.
        
        Args:
            min_value: Minimum allowed value (inclusive)
            max_value: Maximum allowed value (inclusive)
            paths: Optional list of paths to validate (validates all numeric values if None)
            name: Optional validator name
        """
        super().__init__(name or "RangeValidator")
        self.min_value = min_value
        self.max_value = max_value
        self.paths = paths
    
    def applies_to(self, value: Any, path: str) -> bool:
        """Check if this validator applies to the value."""
        if not isinstance(value, (int, float)):
            return False
        if self.paths:
            return any(path.endswith(p) for p in self.paths)
        return True
    
    def validate(
        self,
        value: Any,
        path: str,
        context: Optional[Dict[str, Any]] = None,
        repair: bool = False
    ) -> ValidationResult:
        """Validate that the value is within range."""
        if not isinstance(value, (int, float)):
            return self._create_result(
                ValidationLevel.ERROR,
                f"Expected numeric value, got {type(value).__name__}",
                path,
                original_value=value
            )
        
        # Check minimum
        if self.min_value is not None and value < self.min_value:
            repaired = self.min_value if repair else None
            return self._create_result(
                ValidationLevel.ERROR,
                f"Value {value} is below minimum {self.min_value}",
                path,
                original_value=value,
                repaired_value=repaired,
                was_repaired=repair
            )
        
        # Check maximum
        if self.max_value is not None and value > self.max_value:
            repaired = self.max_value if repair else None
            return self._create_result(
                ValidationLevel.ERROR,
                f"Value {value} is out of range [{self.min_value}, {self.max_value}]",
                path,
                original_value=value,
                repaired_value=repaired,
                was_repaired=repair
            )
        
        return self._create_result(
            ValidationLevel.SUCCESS,
            f"Value {value} is within range",
            path,
            original_value=value
        )


class RequiredFieldValidator(Validator):
    """
    Validates that required fields are present in dictionaries.
    
    Examples:
        >>> validator = RequiredFieldValidator(required_fields=["id", "name"])
        >>> data = {"id": 1, "name": "test", "optional": "value"}
        >>> result = validator.validate(data, "entity", repair=False)
        >>> result.level
        <ValidationLevel.SUCCESS: 'success'>
        
        >>> # Missing required field
        >>> data = {"id": 1}
        >>> result = validator.validate(data, "entity", repair=False)
        >>> result.level
        <ValidationLevel.ERROR: 'error'>
        >>> "name" in result.message
        True
        
        >>> # Test with repair (adds None for missing fields)
        >>> result = validator.validate(data, "entity", repair=True)
        >>> result.was_repaired
        True
        >>> result.repaired_value
        {'id': 1, 'name': None}
    """
    
    def __init__(
        self,
        required_fields: List[str],
        paths: Optional[List[str]] = None,
        name: Optional[str] = None
    ):
        """
        Initialize the required field validator.
        
        Args:
            required_fields: List of field names that must be present
            paths: Optional list of paths to validate
            name: Optional validator name
        """
        super().__init__(name or "RequiredFieldValidator")
        self.required_fields = required_fields
        self.paths = paths
    
    def applies_to(self, value: Any, path: str) -> bool:
        """Check if this validator applies to the value."""
        if not isinstance(value, dict):
            return False
        if self.paths:
            return any(path.endswith(p) for p in self.paths)
        return True
    
    def validate(
        self,
        value: Any,
        path: str,
        context: Optional[Dict[str, Any]] = None,
        repair: bool = False
    ) -> ValidationResult:
        """Validate that required fields are present."""
        if not isinstance(value, dict):
            return self._create_result(
                ValidationLevel.ERROR,
                f"Expected dictionary, got {type(value).__name__}",
                path,
                original_value=value
            )
        
        missing_fields = [f for f in self.required_fields if f not in value]
        
        if missing_fields:
            if repair:
                repaired = dict(value)
                for field in missing_fields:
                    repaired[field] = None
                return self._create_result(
                    ValidationLevel.WARNING,
                    f"Added missing required fields: {', '.join(missing_fields)}",
                    path,
                    original_value=value,
                    repaired_value=repaired,
                    was_repaired=True
                )
            else:
                return self._create_result(
                    ValidationLevel.ERROR,
                    f"Missing required fields: {', '.join(missing_fields)}",
                    path,
                    original_value=value
                )
        
        return self._create_result(
            ValidationLevel.SUCCESS,
            "All required fields present",
            path,
            original_value=value
        )


class PatternValidator(Validator):
    """
    Validates that string values match a regular expression pattern.
    
    Examples:
        >>> import re
        >>> # Email validator
        >>> validator = PatternValidator(
        ...     pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$',
        ...     description="email address"
        ... )
        >>> result = validator.validate("user@example.com", "email", repair=False)
        >>> result.level
        <ValidationLevel.SUCCESS: 'success'>
        
        >>> result = validator.validate("invalid-email", "email", repair=False)
        >>> result.level
        <ValidationLevel.ERROR: 'error'>
        >>> "valid email address" in result.message
        True
    """
    
    def __init__(
        self,
        pattern: str,
        description: str = "pattern",
        paths: Optional[List[str]] = None,
        name: Optional[str] = None
    ):
        """
        Initialize the pattern validator.
        
        Args:
            pattern: Regular expression pattern to match
            description: Human-readable description of what the pattern matches
            paths: Optional list of paths to validate
            name: Optional validator name
        """
        super().__init__(name or "PatternValidator")
        import re
        self.pattern = re.compile(pattern)
        self.pattern_str = pattern
        self.description = description
        self.paths = paths
    
    def applies_to(self, value: Any, path: str) -> bool:
        """Check if this validator applies to the value."""
        if not isinstance(value, str):
            return False
        if self.paths:
            return any(path.endswith(p) for p in self.paths)
        return True
    
    def validate(
        self,
        value: Any,
        path: str,
        context: Optional[Dict[str, Any]] = None,
        repair: bool = False
    ) -> ValidationResult:
        """Validate that the value matches the pattern."""
        if not isinstance(value, str):
            return self._create_result(
                ValidationLevel.ERROR,
                f"Expected string, got {type(value).__name__}",
                path,
                original_value=value
            )
        
        if not self.pattern.match(value):
            return self._create_result(
                ValidationLevel.ERROR,
                f"Value does not match valid {self.description} format",
                path,
                original_value=value,
                metadata={"pattern": self.pattern_str}
            )
        
        return self._create_result(
            ValidationLevel.SUCCESS,
            f"Valid {self.description}",
            path,
            original_value=value
        )