import argparse
from .cli import add_task, list_tasks, mark_done, remove_task, search_tasks


def main(argv=None):
    parser = argparse.ArgumentParser(prog="tasks_app")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list")

    p_add = sub.add_parser("add")
    p_add.add_argument("title")
    p_add.add_argument("description", nargs="?", default="")

    p_done = sub.add_parser("done")
    p_done.add_argument("id")

    p_prio = sub.add_parser("priority")
    p_prio.add_argument("id")
    p_prio.add_argument("priority")

    p_remove = sub.add_parser("remove")
    p_remove.add_argument("id")

    p_search = sub.add_parser("search")
    p_search.add_argument("keyword")

    args = parser.parse_args(argv)

    if args.cmd == "list":
        for t in list_tasks():
            print(t.id, f"[{t.status}]", t.title, "-", t.description)
    elif args.cmd == "add":
        t = add_task(args.title, args.description)
        print(f"Added {t.id} - {t.title}")
    elif args.cmd == "done":
        ok = mark_done(args.id)
        print("Done:" , ok)
    elif args.cmd == "priority":
        # set priority
        ok = __import__(".cli", fromlist=["set_priority"]).set_priority(args.id, args.priority)
        print("Priority set:", ok)
    elif args.cmd == "remove":
        ok = remove_task(args.id)
        print("Removed:", ok)
    elif args.cmd == "search":
        for t in search_tasks(args.keyword):
            print(t.id, t.title)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
