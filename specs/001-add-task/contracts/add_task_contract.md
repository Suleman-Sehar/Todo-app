# API Contract: Add Task

## Endpoint: add_task

### Description
Adds a new task to the in-memory task list with the provided title and optional description.

### Parameters
- **title** (string, required): The title of the task to be added
- **description** (string, optional): The description of the task to be added

### Response
- **id** (integer): The unique identifier assigned to the new task
- **title** (string): The title of the task
- **description** (string): The description of the task
- **is_completed** (boolean): The completion status of the task (default: false)

### Behavior
1. If title is empty or contains only whitespace, return an error
2. Generate a unique ID for the new task (sequential integer)
3. Set is_completed to false by default
4. Add the task to the in-memory task list
5. Return the complete task object with the assigned ID

### Error Cases
- If title is empty: return error message "Title cannot be empty"
- If title contains only whitespace: return error message "Title cannot be empty"