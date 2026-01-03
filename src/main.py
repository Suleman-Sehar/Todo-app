"""
CLI entry point for the todo application.
"""
from typing import Optional
from src.todo import TodoManager
from src.models import Task
from src.utils import validate_title


def display_menu():
    """Display the main menu options."""
    print("\nTodo Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Exit")


def get_user_choice() -> str:
    """Get and validate user menu choice."""
    choice = input("\nEnter your choice: ").strip()
    return choice


def add_task_ui(todo_manager: TodoManager):
    """Handle the UI for adding a new task."""
    print("\n--- Add New Task ---")
    
    # Get task title
    while True:
        title = input("Enter task title: ").strip()
        if validate_title(title):
            break
        else:
            print("Title cannot be empty. Please try again.")
    
    # Get task description (optional)
    description = input("Enter task description (optional): ").strip()
    
    # Add the task
    new_task = todo_manager.add_task(title, description)
    
    print(f"Task added successfully with ID: {new_task.id}")


def view_tasks_ui(todo_manager: TodoManager):
    """Handle the UI for viewing all tasks."""
    print("\n--- View Tasks ---")
    tasks = todo_manager.get_all_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        status = "Completed" if task.is_completed else "Incomplete"
        print(f"ID: {task.id}, Title: {task.title}, Status: {status}")
        if task.description:
            print(f"  Description: {task.description}")


def update_task_ui(todo_manager: TodoManager):
    """Handle the UI for updating a task."""
    print("\n--- Update Task ---")
    tasks = todo_manager.get_all_tasks()
    
    if not tasks:
        print("No tasks found to update.")
        return
    
    task_id = get_task_id("update")
    if not task_id:
        return
    
    task = todo_manager.get_task_by_id(task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return
    
    print(f"Current task: {task.title}")
    
    new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
    new_description = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()
    
    # Update only if user provided new values
    updated_task = todo_manager.update_task(
        task_id,
        title=new_title if new_title else None,
        description=new_description if new_description else None
    )
    
    if updated_task:
        print(f"Task {task_id} updated successfully.")
    else:
        print(f"Failed to update task {task_id}.")


def delete_task_ui(todo_manager: TodoManager):
    """Handle the UI for deleting a task."""
    print("\n--- Delete Task ---")
    tasks = todo_manager.get_all_tasks()
    
    if not tasks:
        print("No tasks found to delete.")
        return
    
    task_id = get_task_id("delete")
    if not task_id:
        return
    
    success = todo_manager.delete_task(task_id)
    if success:
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Task with ID {task_id} not found.")


def mark_task_complete_ui(todo_manager: TodoManager):
    """Handle the UI for marking a task as complete/incomplete."""
    print("\n--- Mark Task Complete/Incomplete ---")
    tasks = todo_manager.get_all_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    task_id = get_task_id("mark complete/incomplete")
    if not task_id:
        return
    
    task = todo_manager.get_task_by_id(task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return
    
    # Toggle completion status
    new_status = not task.is_completed
    updated_task = todo_manager.update_task(task_id, is_completed=new_status)
    
    if updated_task:
        status_text = "completed" if new_status else "incomplete"
        print(f"Task {task_id} marked as {status_text}.")
    else:
        print(f"Failed to update task {task_id}.")


def get_task_id(action: str) -> Optional[int]:
    """Get and validate a task ID from user input."""
    try:
        task_id_input = input(f"Enter task ID to {action}: ").strip()
        if not task_id_input:
            print("No task ID provided.")
            return None
        task_id = int(task_id_input)
        if task_id <= 0:
            print("Task ID must be a positive integer.")
            return None
        return task_id
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return None


def main():
    """Main entry point for the todo application."""
    print("Welcome to the Todo Application!")
    
    # Initialize the todo manager
    todo_manager = TodoManager()
    
    # Main application loop
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == "1":
            add_task_ui(todo_manager)
        elif choice == "2":
            view_tasks_ui(todo_manager)
        elif choice == "3":
            update_task_ui(todo_manager)
        elif choice == "4":
            delete_task_ui(todo_manager)
        elif choice == "5":
            mark_task_complete_ui(todo_manager)
        elif choice == "6":
            print("Thank you for using the Todo Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()