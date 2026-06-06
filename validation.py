"""
validation.py
-------------
Input validation utilities for the Task Management System.
"""


def validate_task_name(task_name):
    """
    Validate the task name provided by the user.
    Returns (is_valid: bool, message: str).
    """
    if len(task_name) == 0:
        return False, "Task name cannot be empty."

    if len(task_name) < 3:
        return False, "Task name must be at least 3 characters long."

    return True, "Valid task name."


def validate_task_id(task_id, tasks):
    """
    Validate that the given task ID exists in the task list.
    Returns (is_valid: bool, message: str).
    """
    try:
        task_id = int(task_id)
    except ValueError:
        return False, "Task ID must be a valid integer."

    if len(tasks) == 0:
        return False, "No tasks available."

    ids = [task["id"] for task in tasks]
    if task_id not in ids:
        return False, f"Task ID {task_id} not found."

    return True, "Valid task ID."