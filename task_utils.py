"""
task_utils.py
-------------
Core utility functions for the Task Management System.

Tasks are stored as a list of dictionaries with the following keys:
    - id       (int):  Unique identifier for the task.
    - name     (str):  Name/description of the task.
    - complete (bool): Whether the task has been completed.
"""

from validation import validate_task_name, validate_task_id


def add_task(tasks, task_name):
    """
    Add a new task to the task list.

    Parameters:
        tasks     (list): The current list of task dictionaries.
        task_name (str):  Name of the new task.

    Returns:
        str: A message indicating success or describing the validation error.
    """
    is_valid, message = validate_task_name(task_name)
    if not is_valid:
        return message

    # Generate a unique ID (1-based, using max existing id + 1)
    new_id = max((task["id"] for task in tasks), default=0) + 1

    task = {
        "id": new_id,
        "name": task_name.strip(),
        "complete": False,
    }
    tasks.append(task)
    return "Task added successfully."


def complete_task(tasks, task_id):
    """
    Mark a task as complete.

    Parameters:
        tasks   (list):      The current list of task dictionaries.
        task_id (int | str): The ID of the task to mark complete.

    Returns:
        str: A message indicating success or describing the validation error.
    """
    is_valid, message = validate_task_id(task_id, tasks)
    if not is_valid:
        return message

    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["complete"] = True
            return "Task marked as complete."

    return "Task not found."


def get_pending_tasks(tasks):
    """
    Retrieve all tasks that have not yet been completed.

    Parameters:
        tasks (list): The current list of task dictionaries.

    Returns:
        list: A list of task dictionaries where complete == False.
    """
    return [task for task in tasks if not task["complete"]]


def track_progress(tasks):
    """
    Calculate and return a summary of overall task progress.

    Parameters:
        tasks (list): The current list of task dictionaries.

    Returns:
        str: A formatted progress report, e.g.
             "Progress: 2/5 tasks completed (40.00%)"
             or "No working currently." when there are no tasks.
    """
    total = len(tasks)
    if total == 0:
        return "No working currently."

    completed = sum(1 for task in tasks if task["complete"])
    percentage = (completed / total) * 100
    return f"Progress: {completed}/{total} tasks completed ({percentage:.2f}%)"