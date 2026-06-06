"""
task_utils.py
-------------
Core utility functions for the Task Management System.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from validation import validate_task_name, validate_task_id


def add_task(tasks, title, description, due_date):
    """
    Add a new task to the task list.

    Returns:
        str: "Task added successfully!" on success, or a validation error message.
    """
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
    """
    Mark a task as complete.

    Returns:
        str: "Task marked as complete!" on success, or a validation error message.
    """
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
    """
    Retrieve all tasks that have not yet been completed.

    Returns:
        list: Tasks where completed == False.
    """
    return [task for task in tasks if not task["completed"]]


def calculate_progress(tasks):
    """
    Calculate the percentage of completed tasks.

    Returns:
        float: Percentage of completed tasks (e.g. 50.0), or 0.0 if no tasks.
    """
    total = len(tasks)
    if total == 0:
        return 0.0

    completed = sum(1 for task in tasks if task["completed"])
    return (completed / total) * 100