from . import services


def main() -> None:
    """Entry point for uv run tasks3: show a brief summary of tasks."""
    tasks = services.list_tasks()
    print(f"Tasks3 app — {len(tasks)} tasks stored")


def inc(n: int) -> int:
    return n + 1
