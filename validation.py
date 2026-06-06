"""
validation.py
-------------
Input validation utilities for the Task Management System.
"""


def validate_task_name(task_name):
    """
    Validate the task name. Raises ValueError if invalid.
    """
    if len(task_name) == 0:
        raise ValueError("Task name cannot be empty.")

    if len(task_name) < 3:
        raise ValueError("Task name must be at least 3 characters long.")

    return True


def validate_task_description(description):
    """
    Validate the task description. Raises ValueError if too long.
    """
    if len(description) > 500:
        raise ValueError("Description must be 500 characters or fewer.")

    return True


def validate_task_id(task_id, tasks):
    """
    Validate that the given task ID exists in the task list.
    Raises ValueError if invalid.
    """
    if len(tasks) == 0:
        raise ValueError("No tasks available.")

    try:
        task_id = int(task_id)
    except ValueError:
        raise ValueError("Task ID must be a valid integer.")

    ids = [task["id"] for task in tasks]
    if task_id not in ids:
        raise ValueError(f"Task ID {task_id} not found.")

    return True