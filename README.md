# csc299-project

# 🧠 tasks1 – Command-Line Task Manager

## Overview
This is a prototype command-line task management system built in Python for the CSC299 final project. It allows users to add, list, and mark tasks as done, with support for priorities, deadlines, and overdue detection. Tasks are stored in a local JSON file for portability and simplicity.

## Features
- ✅ Add tasks with a title
- 📋 List all tasks with status, priority, and deadline
- ⏰ Detect overdue tasks
- ✔️ Mark tasks as done
- 💾 Persistent storage using `tasks.json`

## File Structure
``
Code block expanded
tasks1/
├── main.py        # CLI interface for user interaction
├── service.py     # Core logic for task operations
├── model.py       # Task data model using dataclasses
├── storage.py     # JSON-based persistence layer
└── README.md      # Project documentation
``

## Requirements
- Python 3.8 or higher
- No external dependencies (uses Python standard library)

## How to Run
1. Clone the repository:
   ``bash 
   git clone https://github.com/YOUR_USERNAME/csc299-project.git
   cd csc299-project/tasks1
   ``

2. Run the program:
   ``bash
   python main.py
   ``


## Commands

add <title> – Add a new task with the given title
list – List all tasks
done <id> – Mark a task as done using its ID
help – Show available commands
exit – Exit the program

## Example
``
> python main.py
Welcome to Task Manager (type 'help' for commands)
> add Finish CSC299 prototype
Added task: Finish CSC299 prototype (id=abc12345)
> list
[todo] abc12345 | Finish CSC299 prototype | Priority: medium | Deadline: None
> done abc12345
Marked abc12345 as done.
``

## Notes

Tasks are stored in tasks.json in the same directory.
Overdue tasks are flagged with ⚠️ when listed.
This is an early prototype; future versions may include tagging, searching, and integration with a PKMS.

   
