"""
task_utils.py
-------------
Core utility functions for the Task Management System.
"""

from validation import validate_task_name, validate_task_id


def add_task(tasks, title, description, due_date):
    """Add a new task. Returns 'Task added successfully!' or error message."""
    is_valid, message = validate_task_name(title)
    if not is_valid:
        return message

    new_id = max((task["id"] for task in tasks), default=0) + 1
    task = {
        "id": new_id,
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    return "Task added successfully!"


def complete_task(tasks, task_id):
    """Mark a task complete. Returns 'Task marked as complete!' or error."""
    is_valid, message = validate_task_id(task_id, tasks)
    if not is_valid:
        return message

    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return "Task marked as complete!"
    return "Task not found."


def get_pending_tasks(tasks):
    """Return list of incomplete tasks."""
    return [task for task in tasks if not task["completed"]]


def calculate_progress(tasks):
    """Return float percentage of completed tasks."""
    total = len(tasks)
    if total == 0:
        return 0.0
    completed = sum(1 for task in tasks if task["completed"])
    return (completed / total) * 100


def validate_input(value, tasks):
    """Validate input value and task list."""
    try:
        value = int(value)
    except ValueError:
        return False, "Invalid input."
    if len(tasks) == 0:
        return False, "No tasks available."
    return True, "Valid."