"""
task_utils.py
-------------
Core utility functions for the Task Management System.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from validation import validate_task_name, validate_task_description, validate_task_id


def add_task(tasks, title, description, due_date):
    """Add a new task. Returns 'Task added successfully!' or error message."""
    try:
        validate_task_name(title)
        validate_task_description(description)
    except ValueError as e:
        return str(e)

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
    try:
        validate_task_id(task_id, tasks)
    except ValueError as e:
        return str(e)

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