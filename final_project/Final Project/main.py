#!/usr/bin/env python3
"""Interactive front-end for the Final Project tasks app.

Run this from the repository root as:

  /Users/alexle/csc299-project/.venv/bin/python "Final Project/main.py"

The script will prepend the package src directory to sys.path so it can import
the `tasks_app` package in-place.
"""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
sys.path.insert(0, str(SRC))

from tasks_app import cli


def show_tasks():
    tasks = cli.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        due = f" | Due: {task.due_date}" if task.due_date else ""
        print(f"[{task.status.upper()}] {task.id[:8]} | {task.title} | Priority: {task.priority}{due}")


def repl():
    print("Welcome to Task Manager (type 'help' for commands)")
    while True:
        try:
            cmd = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not cmd:
            continue
        parts = cmd.split(maxsplit=1)
        cmd_name = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if cmd_name == "exit":
            break
        elif cmd_name == "help":
            print("Commands: add <title> [| description], list, done <id|prefix>, search <keyword>, remove <id|prefix>, exit")
        elif cmd_name == "add":
            # support: add Title | optional description
            title = arg
            desc = ""
            if "|" in arg:
                title, desc = [p.strip() for p in arg.split("|", 1)]
            if not title:
                print("Usage: add <title> [| description]")
                continue
            t = cli.add_task(title, desc)
            print(f"Added task: {t.title} (id={t.id[:8]})")
        elif cmd_name == "list":
            show_tasks()
        elif cmd_name == "done":
            if not arg:
                print("Please provide a task ID. Usage: done <id>")
                continue
            ok = cli.mark_done(arg)
            print(f"Marked done: {ok}")
        elif cmd_name == "search":
            if not arg:
                print("Please provide a search keyword. Usage: search <keyword>")
                continue
            res = cli.search_tasks(arg)
            if not res:
                print("No matches.")
            else:
                for t in res:
                    print(f"{t.id[:8]} | {t.title} | {t.status}")
        elif cmd_name == "remove":
            if not arg:
                print("Please provide a task ID. Usage: remove <id>")
                continue
            ok = cli.remove_task(arg)
            print(f"Removed: {ok}")
        else:
            print("Unknown command. Type 'help'.")


def main():
    repl()


if __name__ == "__main__":
    main()
