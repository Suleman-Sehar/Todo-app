"""
Core task operations for the todo application.
"""
from typing import List, Optional
from src.models import Task


class TodoManager:
    """
    Manages the in-memory task list and provides core task operations.
    """
    
    def __init__(self):
        """Initialize the todo manager with an empty task list."""
        self.tasks: List[Task] = []
    
    def add_task(self, title: str, description: Optional[str] = "") -> Task:
        """
        Add a new task to the in-memory task list.
        
        Args:
            title: The title of the task (required)
            description: The description of the task (optional)
            
        Returns:
            Task: The newly created task with a unique ID and is_completed=False
        """
        from src.utils import generate_id

        # Create a new task with a unique ID
        task_id = generate_id()
        new_task = Task(
            id=task_id,
            title=title,
            description=description or "",
            is_completed=False
        )
        
        # Add the task to the in-memory list
        self.tasks.append(new_task)
        
        return new_task
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks from the in-memory list.
        
        Returns:
            List[Task]: A list of all tasks
        """
        return self.tasks
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            Task: The task with the specified ID, or None if not found
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None, 
                   description: Optional[str] = None, 
                   is_completed: Optional[bool] = None) -> Optional[Task]:
        """
        Update an existing task.
        
        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)
            is_completed: New completion status (optional)
            
        Returns:
            Task: The updated task, or None if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if is_completed is not None:
                task.is_completed = is_completed
            return task
        return None
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False