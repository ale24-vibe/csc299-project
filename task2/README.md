
### README.md

# 🧠 Task Manager v2 – Enhanced CLI Task System

## Overview
This is the second iteration of the Task Manager prototype for the CSC299 final project. It builds upon the original version by adding support for task descriptions, deadlines, priorities, and tags. Tasks are stored in a JSON file and managed through a terminal-based interface.

## Features
- ✅ Add tasks with title, description, deadline, priority, and tags
- 📋 List all tasks with status, priority, and deadline
- ⏰ Detect overdue tasks
- ✔️ Mark tasks as done
- 🔍 Search tasks by keyword (title or description)
- 🏷️ Search tasks by tag

## File Structure
```
tasks2/
├── main.py        # CLI interface for user interaction
├── service.py     # Core logic for task operations
├── model.py       # Task data model using dataclasses
├── storage.py     # JSON-based persistence layer
└── tasks.json     # Auto-generated task data file
```

## Requirements
- Python 3.8 or higher
- No external dependencies (uses Python standard library)

## How to Run
1. Navigate to the `tasks2` directory:
   ```bash
   cd csc299-project/tasks2
   ```

2. Run the task manager:
   ```bash
   python3 main.py
   ```

## Commands
- `add` – Add a new task (interactive prompts for details)
- `list` – List all tasks
- `done <id>` – Mark a task as done using its ID
- `search <keyword>` – Search tasks by keyword in title or description
- `tag <tag>` – Search tasks by tag
- `help` – Show available commands
- `exit` – Exit the program

## Example Usage
```bash
> python3 main.py
Welcome to Task Manager v2 (type 'help' for commands)
> add
Title: Finish essay
Description: Final draft due Monday
Deadline: 2025-11-01
Priority: high
Add tags? (y/n): y
Tags (comma-separated): school, urgent
Added task: Finish essay (id=abc12345)

> list
[todo] abc12345 | Finish essay | Priority: high | Deadline: 2025-11-01 ⚠️
  Description: Final draft due Monday
  Tags: school, urgent

> search essay
[todo] abc12345 | Finish essay | Priority: high | Deadline: 2025-11-01 ⚠️
  Description: Final draft due Monday
  Tags: school, urgent

> tag urgent
[todo] abc12345 | Finish essay | Priority: high | Deadline: 2025-11-01 ⚠️
  Description: Final draft due Monday
  Tags: school, urgent
```

## Notes
- Tasks are stored in `tasks.json` in the same directory.
- Overdue tasks are flagged with ⚠️.
- This version sets the foundation for future integration with PKMS and AI agents.

