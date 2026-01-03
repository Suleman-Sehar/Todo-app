"""
Utility functions for the todo application.
"""
import itertools
from typing import Optional


# Global counter for generating unique IDs
_id_counter = itertools.count(1)


def generate_id() -> int:
    """
    Generate a unique task ID.
    
    Returns:
        int: A unique sequential ID for a new task
    """
    return next(_id_counter)


def validate_title(title: str) -> bool:
    """
    Validate that the title is not empty or contain only whitespace.
    
    Args:
        title: The title to validate
        
    Returns:
        bool: True if title is valid, False otherwise
    """
    return bool(title and title.strip())


def reset_id_counter(start: int = 1) -> None:
    """
    Reset the ID counter (used for testing purposes).
    
    Args:
        start: The starting value for the counter
    """
    global _id_counter
    _id_counter = itertools.count(start)