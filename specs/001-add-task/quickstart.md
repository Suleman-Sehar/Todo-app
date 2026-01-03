# Quickstart Guide: Add Task Feature

## Environment Setup

1. Ensure Python 3.13+ is installed
2. Install UV if not already installed:
   ```bash
   pip install uv
   ```
3. Create and activate the virtual environment:
   ```bash
   uv venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

## Running the Application

1. Navigate to the project root directory
2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Run the application:
   ```bash
   python src/main.py
   ```

## Using the Add Task Feature

1. When the application starts, you'll see a menu with options
2. Select the "Add Task" option (usually option 1)
3. Enter the task title when prompted (required)
4. Optionally enter a task description when prompted
5. The system will confirm that the task has been added
6. The new task will appear in the task list with a unique ID and "Incomplete" status

## Example Interaction

```
Todo Application
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Exit

Enter your choice: 1

Enter task title: Buy groceries

Enter task description (optional): Need to buy milk, bread, and eggs

Task added successfully with ID: 1
```