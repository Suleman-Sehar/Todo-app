"""
Simple test script to verify the Add Task functionality.
"""
from src.todo import TodoManager
from src.models import Task


def test_add_task_functionality():
    """Test the add task functionality directly."""
    print("Testing Add Task functionality...")
    
    # Create a todo manager
    todo_manager = TodoManager()
    
    # Test adding a task with title only
    print("\n1. Adding task with title only...")
    task1 = todo_manager.add_task("Test Task 1")
    print(f"   Created task: ID={task1.id}, Title='{task1.title}', Description='{task1.description}', Completed={task1.is_completed}")
    
    # Test adding a task with title and description
    print("\n2. Adding task with title and description...")
    task2 = todo_manager.add_task("Test Task 2", "This is a test description")
    print(f"   Created task: ID={task2.id}, Title='{task2.title}', Description='{task2.description}', Completed={task2.is_completed}")
    
    # Test adding multiple tasks to verify unique IDs
    print("\n3. Adding multiple tasks to verify unique IDs...")
    task3 = todo_manager.add_task("Test Task 3", "Third task")
    task4 = todo_manager.add_task("Test Task 4")
    print(f"   Task 3: ID={task3.id}, Title='{task3.title}'")
    print(f"   Task 4: ID={task4.id}, Title='{task4.title}'")
    
    # Verify all tasks are stored
    print("\n4. Verifying all tasks are stored...")
    all_tasks = todo_manager.get_all_tasks()
    print(f"   Total tasks in manager: {len(all_tasks)}")
    for task in all_tasks:
        print(f"   - ID: {task.id}, Title: '{task.title}', Completed: {task.is_completed}")
    
    print("\nAdd Task functionality test completed successfully!")


if __name__ == "__main__":
    test_add_task_functionality()