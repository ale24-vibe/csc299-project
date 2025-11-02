import services

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        overdue = "⚠️" if t.is_overdue() else ""
        print(f"[{t.status.upper()}] {t.id[:8]} | {t.title} | Priority: {t.priority} | Deadline: {t.deadline} {overdue}")
        if t.description:
            print(f"  Description: {t.description}")
        if t.tags:
            print(f"  Tags: {', '.join(t.tags)}")

def main():
    print("Welcome to Task Manager v2 (type 'help' for commands)")
    while True:
        cmd = input("> ").strip()
        if cmd == "exit":
            break
        elif cmd.startswith("add"):
            title = input("Title: ").strip()
            description = input("Description: ").strip()
            deadline = input("Deadline (YYYY-MM-DD or ISO format): ").strip()
            priority = input("Priority (low/medium/high): ").strip().lower()
            add_tags = input("Add tags? (y/n): ").strip().lower()
            if add_tags == "y":
                tags = [t.strip() for t in input("Tags (comma-separated): ").strip().split(",") if t.strip()]
            else:
                tags = []
            task = services.add_task(title, description, deadline, priority, [tag.strip() for tag in tags])
            print(f"Added task: {task.title} (id={task.id[:8]})")
        elif cmd == "list":
            tasks = services.list_tasks()
            show_tasks(tasks)
        elif cmd.startswith("done"):
            try:
                _, task_id = cmd.split(maxsplit=1)
            except ValueError:
                print("Please provide a task ID. Usage: done <id>")
                continue
            ok = services.mark_done(task_id)
            if ok:
                print(f"Marked {task_id} as done.")
            else:
                print(f"No task found matching id: {task_id}")
        elif cmd.startswith("search"):
            _, keyword = cmd.split(maxsplit=1)
            results = services.search_tasks(keyword)
            show_tasks(results)
        elif cmd.startswith("tag"):
            _, tag = cmd.split(maxsplit=1)
            results = services.search_by_tag(tag)
            show_tasks(results)
        elif cmd == "help":
            print("Commands:")
            print("  add              - Add a new task")
            print("  list             - List all tasks")
            print("  done <id>        - Mark a task as done")
            print("  search <keyword> - Search tasks by keyword")
            print("  tag <tag>        - Search tasks by tag")
            print("  exit             - Exit the program")
        else:
            print("Unknown command. Type 'help'.")

if __name__ == "__main__":
    main()