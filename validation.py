# validation.py

def validate_task_name(title):
    """Validate a task title.
    
    Returns:
        tuple: (is_valid, message)
    """
    if not isinstance(title, str) or not title.strip():
        return False, "Title must be a non-empty string."
    return True, "Valid."


def validate_task_id(task_id, tasks):
    """Validate a task ID against the existing tasks list.
    
    Returns:
        tuple: (is_valid, message)
    """
    try:
        task_id = int(task_id)
    except (ValueError, TypeError):
        return False, "Invalid task ID."
    if not any(task["id"] == task_id for task in tasks):
        return False, "Task not found."
    return True, "Valid."


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