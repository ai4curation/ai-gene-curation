"""Tree walker for applying validators to nested data structures."""

from typing import Any, Dict, List, Optional, Union, Callable, Generator, Tuple
from .base import Validator, ValidationResult, ValidationReport


def walk_tree(
    data: Any,
    path: str = "",
    parent_context: Optional[Dict[str, Any]] = None
) -> Generator[Tuple[Any, str, Dict[str, Any]], None, None]:
    """
    Walk a nested data structure, yielding (value, path, context) tuples.
    
    This function performs a depth-first traversal of nested dicts and lists,
    maintaining the path to each node for precise error reporting.
    
    Args:
        data: The data structure to walk
        path: Current path in the structure (e.g., "primary_functions[0].activity.term")
        parent_context: Context from parent nodes
        
    Yields:
        Tuples of (value, path, context) for each node in the tree
        
    Examples:
        >>> data = {"a": {"b": 1}, "c": [2, 3]}
        >>> paths = []
        >>> for value, path, ctx in walk_tree(data):
        ...     if path:  # Skip root
        ...         paths.append(path)
        >>> sorted(paths)
        ['a', 'a.b', 'c', 'c[0]', 'c[1]']
        
        >>> # Walk nested structure with arrays
        >>> data = {"terms": [{"id": "GO:0001", "label": "test"}]}
        >>> for value, path, ctx in walk_tree(data):
        ...     if path == "terms[0].id":
        ...         print(f"Found term ID: {value}")
        Found term ID: GO:0001
        
        >>> # Context includes depth information
        >>> data = {"a": {"b": {"c": 1}}}
        >>> for value, path, ctx in walk_tree(data):
        ...     if path == "a.b.c":
        ...         print(f"Depth: {ctx['depth']}")
        Depth: 2
    """
    # Build context for this node
    context = parent_context or {}
    context = {**context, "parent_path": path, "depth": path.count(".") + path.count("[")}
    
    # Yield current node
    yield data, path, context
    
    # Recurse into structure
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            yield from walk_tree(value, new_path, context)
            
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{path}[{i}]"
            yield from walk_tree(item, new_path, context)


def validate_tree(
    data: Any,
    validators: List[Validator],
    repair: bool = False,
    path_filter: Optional[Callable[[str], bool]] = None,
    report: Optional[ValidationReport] = None
) -> Tuple[Any, ValidationReport]:
    """
    Validate and optionally repair a nested data structure.
    
    Args:
        data: The data structure to validate
        validators: List of validators to apply
        repair: Whether to attempt repairs
        path_filter: Optional function to filter which paths to validate
        report: Optional existing report to append to
        
    Returns:
        Tuple of (possibly modified data, validation report)
    """
    if report is None:
        report = ValidationReport()
    
    # Create a mutable copy if we're repairing
    if repair:
        data = _deep_copy_mutable(data)
    
    # Walk the tree and apply validators
    for value, path, context in walk_tree(data):
        # Skip if path filter excludes this path
        if path_filter and not path_filter(path):
            continue
        
        # Apply each validator that matches this value
        for validator in validators:
            if validator.applies_to(value, path):
                results = validator.validate(value, path, context, repair)
                
                # Handle single result or list of results
                if isinstance(results, ValidationResult):
                    results = [results]
                
                for result in results:
                    report.add_result(result)
                    
                    # Apply repair if one was made
                    if repair and result.was_repaired and result.repaired_value is not None:
                        _set_value_at_path(data, path, result.repaired_value)
    
    report.finalize()
    return data, report


def _deep_copy_mutable(obj: Any) -> Any:
    """Create a deep mutable copy of an object."""
    if isinstance(obj, dict):
        return {k: _deep_copy_mutable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_deep_copy_mutable(item) for item in obj]
    else:
        return obj


def _set_value_at_path(data: Any, path: str, value: Any) -> None:
    """
    Set a value at a specific path in a nested data structure.
    
    This function navigates through the data structure using the path
    and sets the value at the specified location.
    
    Args:
        data: The data structure to modify (must be mutable)
        path: Path to the value (e.g., "primary_functions[0].activity.term")
        value: The new value to set
        
    Examples:
        >>> data = {"a": {"b": 1}}
        >>> _set_value_at_path(data, "a.b", 2)
        >>> data["a"]["b"]
        2
        
        >>> data = {"items": [{"id": 1}, {"id": 2}]}
        >>> _set_value_at_path(data, "items[1].id", 3)
        >>> data["items"][1]["id"]
        3
        
        >>> # Complex nested path
        >>> data = {"terms": [{"props": {"label": "old"}}]}
        >>> _set_value_at_path(data, "terms[0].props.label", "new")
        >>> data["terms"][0]["props"]["label"]
        'new'
    """
    if not path:
        # Can't replace root
        return
    
    # Parse the path into segments
    segments = []
    current = ""
    in_bracket = False
    
    for char in path:
        if char == "[":
            if current:
                segments.append(current)
                current = ""
            in_bracket = True
        elif char == "]":
            if current:
                segments.append(int(current))
                current = ""
            in_bracket = False
        elif char == "." and not in_bracket:
            if current:
                segments.append(current)
                current = ""
        else:
            current += char
    
    if current:
        segments.append(current)
    
    # Navigate to the parent and set the value
    parent = data
    for segment in segments[:-1]:
        if isinstance(segment, int):
            parent = parent[segment]
        else:
            parent = parent[segment]
    
    # Set the final value
    final_key = segments[-1]
    if isinstance(final_key, int):
        parent[final_key] = value
    else:
        parent[final_key] = value


def validate_file(
    file_path: str,
    validators: List[Validator],
    repair: bool = False,
    output_path: Optional[str] = None
) -> ValidationReport:
    """
    Validate a YAML file with the given validators.
    
    Args:
        file_path: Path to the file to validate
        validators: List of validators to apply
        repair: Whether to attempt repairs
        output_path: Optional path to write repaired file to
        
    Returns:
        ValidationReport with results
    """
    from pathlib import Path
    from yaml import safe_load, safe_dump
    
    file_path = Path(file_path)
    
    # Load the file
    with open(file_path) as f:
        data = safe_load(f)
    
    # Validate and repair
    repaired_data, report = validate_tree(data, validators, repair)
    report.file_path = str(file_path)
    
    # Write repaired file if requested
    if repair and output_path:
        with open(output_path, 'w') as f:
            safe_dump(repaired_data, f, sort_keys=False, allow_unicode=True)
    
    return report