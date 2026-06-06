def validate_task(description):
    """Validate a task description.
    
    Args:
        description (str): The task description to validate.
        
    Raises:
        ValueError: If description is not a string or exceeds 500 characters.
    """
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    
    if len(description) > 500:
        raise ValueError("Description must be 500 characters or fewer.")
    
    return True