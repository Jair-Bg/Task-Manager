"""
main.py
-------
Entry point for the Task Management System.

Provides a simple menu-driven interface that lets users:
    1. Add a task
    2. Mark a task as complete
    3. View pending tasks
    4. Track progress
    5. Exit
"""

from task_utils import add_task, complete_task, get_pending_tasks, track_progress


def display_menu():
    """Print the main menu options to the console."""
    print("\n===== Task Management System =====")
    print("1. Add a task")
    print("2. Mark a task as complete")
    print("3. View pending tasks")
    print("4. Track progress")
    print("5. Exit")
    print("==================================")


def main():
    """Run the Task Management System application loop."""
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            # Add a task
            task_name = input("Enter the task name: ")
            message = add_task(tasks, task_name)
            print(message)

        elif choice == "2":
            # Mark a task as complete
            pending = get_pending_tasks(tasks)
            if not pending:
                print("No pending tasks to complete.")
            else:
                print("\nPending Tasks:")
                for task in pending:
                    print(f"  ID: {task['id']} | {task['name']}")
                task_id = input("Enter the task ID to mark as complete: ")
                message = complete_task(tasks, task_id)
                print(message)

        elif choice == "3":
            # View pending tasks
            pending = get_pending_tasks(tasks)
            if not pending:
                print("No pending tasks.")
            else:
                print("\nPending Tasks:")
                for task in pending:
                    print(f"  ID: {task['id']} | {task['name']}")

        elif choice == "4":
            # Track progress
            print(track_progress(tasks))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()