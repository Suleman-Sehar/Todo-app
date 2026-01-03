"""
Demo script to showcase the functionality of the todo application.
"""
from src.todo import TodoManager
from src.utils import reset_id_counter


def demo_add_task_feature():
    """Demonstrate the Add Task functionality."""
    print("=== Todo Application Demo ===")
    print("Demonstrating the Add Task feature...\n")
    
    # Create a fresh todo manager
    reset_id_counter()  # Reset ID counter for predictable results
    todo_manager = TodoManager()
    
    # Demo 1: Adding a task with title only
    print("1. Adding a task with title only:")
    task1 = todo_manager.add_task("Buy groceries")
    print(f"   Added task: ID={task1.id}, Title='{task1.title}', Description='{task1.description}', Completed={task1.is_completed}")

    # Demo 2: Adding a task with title and description
    print("\n2. Adding a task with title and description:")
    task2 = todo_manager.add_task("Complete project", "Finish the todo app implementation")
    print(f"   Added task: ID={task2.id}, Title='{task2.title}', Description='{task2.description}', Completed={task2.is_completed}")

    # Demo 3: Adding another task to show unique IDs
    print("\n3. Adding another task to demonstrate unique ID generation:")
    task3 = todo_manager.add_task("Call mom", "Catch up on family news")
    print(f"   Added task: ID={task3.id}, Title='{task3.title}', Description='{task3.description}', Completed={task3.is_completed}")

    # Demo 4: View all tasks
    print("\n4. Viewing all tasks:")
    all_tasks = todo_manager.get_all_tasks()
    print(f"   Total tasks: {len(all_tasks)}")
    for task in all_tasks:
        status = "Completed" if task.is_completed else "Incomplete"
        print(f"   - ID: {task.id}, Title: '{task.title}', Status: {status}")
        if task.description:
            print(f"     Description: {task.description}")

    # Demo 5: Demonstrate validation
    print("\n5. Demonstrating title validation:")
    try:
        # This should raise an error
        invalid_task = todo_manager.add_task("   ")  # Only whitespace
        print("   This should not print")
    except ValueError as e:
        print(f"   Correctly rejected invalid title: {e}")

    print("\n=== Demo Complete ===")
    print("The Add Task feature is working correctly!")
    print("The full application provides a CLI menu for user interaction.")


if __name__ == "__main__":
    demo_add_task_feature()