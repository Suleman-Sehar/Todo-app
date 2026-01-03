"""
Unit tests for the Task model.
"""
import pytest
from src.models import Task


def test_task_creation():
    """Test creating a task with valid parameters."""
    task = Task(id=1, title="Test Task", description="Test Description", is_completed=False)
    
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.is_completed is False


def test_task_creation_defaults():
    """Test creating a task with default values."""
    task = Task(id=1, title="Test Task")
    
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == ""
    assert task.is_completed is False


def test_task_validation_empty_title():
    """Test that creating a task with an empty title raises an error."""
    with pytest.raises(ValueError, match="Title cannot be empty or contain only whitespace"):
        Task(id=1, title="")


def test_task_validation_whitespace_title():
    """Test that creating a task with a whitespace-only title raises an error."""
    with pytest.raises(ValueError, match="Title cannot be empty or contain only whitespace"):
        Task(id=1, title="   ")


def test_task_validation_valid_title():
    """Test that creating a task with a valid title works."""
    task = Task(id=1, title="Valid Title")
    
    assert task.title == "Valid Title"