"""
main.py
-------
Task Management System - all modules combined for compatibility.
"""

# ── validation.py logic ──────────────────────────────────────────────

def validate_task_name(task_name):
    if not isinstance(task_name, str):
        return False, "Task name must be a string."
    task_name = task_name.strip()
    if len(task_name) == 0:
        return False, "Task name cannot be empty."
    if len(task_name) < 3:
        return False, "Task name must be at least 3 characters long."
    return True, "Valid task name."


def validate_task_id(task_id, tasks):
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


# ── task_utils.py logic ──────────────────────────────────────────────

def add_task(tasks, title, description, due_date):
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
    return [task for task in tasks if not task["completed"]]


def calculate_progress(tasks):
    total = len(tasks)
    if total == 0:
        return 0.0
    completed = sum(1 for task in tasks if task["completed"])
    return (completed / total) * 100


# ── main menu ────────────────────────────────────────────────────────

def display_menu():
    print("\n===== Task Management System =====")
    print("1. Add a task")
    print("2. Mark a task as complete")
    print("3. View pending tasks")
    print("4. Track progress")
    print("5. Exit")
    print("==================================")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            print(add_task(tasks, title, description, due_date))

        elif choice == "2":
            pending = get_pending_tasks(tasks)
            if not pending:
                print("No pending tasks to complete.")
            else:
                print("\nPending Tasks:")
                for task in pending:
                    print(f"  ID: {task['id']} | {task['title']} | Due: {task['due_date']}")
                task_id = input("Enter the task ID to mark as complete: ")
                print(complete_task(tasks, task_id))

        elif choice == "3":
            pending = get_pending_tasks(tasks)
            if not pending:
                print("No pending tasks.")
            else:
                print("\nPending Tasks:")
                for task in pending:
                    print(f"  ID: {task['id']} | {task['title']} | Due: {task['due_date']}")

        elif choice == "4":
            print(calculate_progress(tasks))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()