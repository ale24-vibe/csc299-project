"""Console entrypoint for the minimal tasks_manager.

Usage examples (after setting PYTHONPATH=tasks5/src or installing the package):
  python -m tasks_manager add "Title" "Description"
  python -m tasks_manager list
  python -m tasks_manager done <id-prefix>
  python -m tasks_manager remove <id-prefix>
  python -m tasks_manager search <keyword>
"""
from __future__ import annotations

import argparse
import sys
from typing import Iterable

from .cli import add_task, list_tasks, mark_done, remove_task, search_tasks


def _print_tasks(tasks: Iterable):
    for t in tasks:
        print(f"{t.id}  [{t.status}] {t.title} - {t.description}")


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    p = argparse.ArgumentParser(prog="tasks_manager")
    sub = p.add_subparsers(dest="cmd")

    a_add = sub.add_parser("add", help="Add a task")
    a_add.add_argument("title")
    a_add.add_argument("description", nargs="?", default="")

    a_list = sub.add_parser("list", help="List tasks")

    a_done = sub.add_parser("done", help="Mark task done")
    a_done.add_argument("id")

    a_remove = sub.add_parser("remove", help="Remove task")
    a_remove.add_argument("id")

    a_search = sub.add_parser("search", help="Search tasks")
    a_search.add_argument("keyword")

    args = p.parse_args(argv)
    if not args.cmd:
        p.print_help()
        return 1

    if args.cmd == "add":
        t = add_task(args.title, args.description)
        print(f"Added {t.id} — {t.title}")
        return 0

    if args.cmd == "list":
        _print_tasks(list_tasks())
        return 0

    if args.cmd == "done":
        ok = mark_done(args.id)
        print("OK" if ok else "Not found")
        return 0 if ok else 2

    if args.cmd == "remove":
        ok = remove_task(args.id)
        print("Removed" if ok else "Not found")
        return 0 if ok else 2

    if args.cmd == "search":
        _print_tasks(search_tasks(args.keyword))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
