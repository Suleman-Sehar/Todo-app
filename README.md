# Command-Line Todo Application

A simple command-line todo application built with Python that stores tasks in memory.

## Features

- Add new tasks with title and optional description
- View all tasks with their completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete

## Prerequisites

- Python 3.13+
- UV for environment management (optional but recommended)

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   uv venv .venv  # or python -m venv .venv
   ```
3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   uv pip install -r requirements.txt  # if you have a requirements.txt file
   # or just run the application directly
   ```

## Usage

Run the application:
```bash
python -m src.main
```

Follow the on-screen menu to interact with the application:
1. Add Task - Add a new task with a title and optional description
2. View Tasks - See all tasks with their status
3. Update Task - Modify an existing task
4. Delete Task - Remove a task
5. Mark Task Complete - Toggle task completion status
6. Exit - Quit the application

## Project Structure

```
src/
├── main.py          # CLI entry point and user interaction loop
├── todo.py          # Core task operations (Add, View, Update, Delete, Mark Complete)
├── models.py        # Task data structure and validation
└── utils.py         # Input validation, ID generation, display helpers

tests/
├── unit/
│   ├── test_models.py
│   ├── test_todo.py
│   └── test_utils.py
└── contract/
    └── test_add_task.py
```

## Development

This project follows an agentic development approach using Qwen Code, with all code generated automatically based on feature specifications. All prompts, plans, and task iterations are documented to maintain traceability.

## Testing

Run all tests:
```bash
python -m pytest tests/
```

Run specific test file:
```bash
python -m pytest tests/unit/test_models.py
```

## Architecture

- **Models**: Task data structure with validation
- **Utils**: Helper functions for ID generation and input validation
- **Todo**: Core business logic for task management
- **Main**: CLI interface and user interaction