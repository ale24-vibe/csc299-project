import services

def show_tasks():
    tasks = services.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        overdue = "⚠️" if task.is_overdue() else ""
        print(f"[{task.status.upper()}] {task.id[:8]} | {task.title} | "
              f"Priority: {task.priority} | Deadline: {task.deadline} {overdue}")

def main():
    print("Welcome to Task Manager (type 'help' for commands)")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "exit":
            break
        elif cmd.startswith("add"):
            title = cmd.replace("add", "", 1).strip()
            task = services.add_task(title)
            print(f"Added task: {task.title} (id={task.id[:8]})")
        elif cmd == "list":
            show_tasks()
        elif cmd.startswith("done"):
            try:
                _, task_id = cmd.split(maxsplit=1)
            except ValueError:
                print("Please provide a task ID. Usage: done <id>")
                continue
            services.mark_done(task_id)
            print(f"Marked {task_id} as done.")
        elif cmd == "help":
            print("Commands: add <title>, list, done <id>, exit")
        else:
            print("Unknown command. Type 'help'.")

if __name__ == "__main__":
    main()