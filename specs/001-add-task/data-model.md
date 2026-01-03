# Data Model: Add Task Feature

## Task Entity

### Fields
- **id**: Integer (unique identifier, auto-incrementing from 1)
- **title**: String (required, non-empty)
- **description**: String (optional, can be empty)
- **is_completed**: Boolean (default: False)

### Validation Rules
- Title must not be empty or contain only whitespace
- ID must be unique within the current session
- is_completed defaults to False when creating a new task

### State Transitions
- New Task: id (auto-generated), title (from user), description (from user or empty), is_completed (False)
- When task is marked complete: is_completed changes from False to True
- When task is marked incomplete: is_completed changes from True to False

## In-Memory Storage Structure
- Tasks will be stored in a Python list
- Each task will be represented as a dictionary with the above fields
- The list will be maintained in the todo.py module