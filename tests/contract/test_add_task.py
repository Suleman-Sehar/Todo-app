"""
Contract tests for add_task functionality.
"""
from src.todo import TodoManager
from src.models import Task
from src.utils import reset_id_counter


def test_add_task_basic():
    """Test basic task addition functionality."""
    reset_id_counter()  # Reset ID counter to ensure predictable IDs
    todo_manager = TodoManager()

    # Add a task with title only
    task = todo_manager.add_task("Test Task")

    # Verify the task was created correctly
    assert isinstance(task, Task)
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == ""
    assert task.is_completed is False

    # Verify the task was added to the manager
    all_tasks = todo_manager.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0] == task


def test_add_task_with_description():
    """Test adding a task with both title and description."""
    reset_id_counter()  # Reset ID counter to ensure predictable IDs
    todo_manager = TodoManager()

    # Add a task with title and description
    task = todo_manager.add_task("Test Task", "Test Description")

    # Verify the task was created correctly
    assert isinstance(task, Task)
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.is_completed is False

    # Verify the task was added to the manager
    all_tasks = todo_manager.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0] == task


def test_add_multiple_tasks():
    """Test adding multiple tasks with sequential IDs."""
    reset_id_counter()  # Reset ID counter to ensure predictable IDs
    todo_manager = TodoManager()

    # Add first task
    task1 = todo_manager.add_task("First Task", "Description 1")

    # Add second task
    task2 = todo_manager.add_task("Second Task", "Description 2")

    # Verify both tasks have correct properties
    assert task1.id == 1
    assert task1.title == "First Task"
    assert task1.description == "Description 1"

    assert task2.id == 2
    assert task2.title == "Second Task"
    assert task2.description == "Description 2"

    # Verify both tasks are in the manager
    all_tasks = todo_manager.get_all_tasks()
    assert len(all_tasks) == 2
    assert all_tasks[0] == task1
    assert all_tasks[1] == task2


def test_add_task_default_completion_status():
    """Test that new tasks have is_completed set to False by default."""
    reset_id_counter()  # Reset ID counter to ensure predictable IDs
    todo_manager = TodoManager()

    task = todo_manager.add_task("Test Task")

    assert task.is_completed is False


def test_add_task_empty_description_handling():
    """Test that empty descriptions are handled properly."""
    reset_id_counter()  # Reset ID counter to ensure predictable IDs
    todo_manager = TodoManager()

    # Add task with explicitly empty description
    task = todo_manager.add_task("Test Task", "")

    assert task.description == ""

    # Add task with None as description (should default to empty string)
    task2 = todo_manager.add_task("Test Task 2", None)

    # The implementation should handle None as empty string
    assert task2.description == ""