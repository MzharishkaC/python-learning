from tasks import (
    add_task,
    get_tasks,
    delete_task,
    update_task,
    get_task_by_id,
    find_task,
    get_tasks_by_status,
    change_task_status,
    get_tasks_stats,
    delete_tasks_by_status,
)


def show_tasks(tasks_list: list) -> None:
    if not tasks_list:
        print("No tasks found.")
        return

    for task in tasks_list:
        print(
            f'ID: {task["id"]} | '
            f'Title: {task["title"]} | '
            f'Status: {task["status"]}'
        )


def main() -> None:
    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Show all tasks")
        print("2. Add task")
        print("3. Change task status")
        print("4. Update task")
        print("5. Delete task")
        print("6. Find task")
        print("7. Show statistics")
        print("8. Show tasks by status")
        print("9. Delete tasks by status")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(get_tasks())

        elif choice == "2":
            title = input("Enter task title: ").strip()

            if not title:
                print("Task title cannot be empty.")
                continue

            task = add_task(title)
            print("Task created:")
            show_tasks([task])

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID: "))
            except ValueError:
                print("ID must be a number.")
                continue

            status = input("Enter new status: ").strip()

            if not status:
                print("Status cannot be empty.")
                continue

            if change_task_status(task_id, status):
                print("Task status updated.")
            else:
                print("Task not found.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID: "))
            except ValueError:
                print("ID must be a number.")
                continue

            new_title = input("Enter new title: ").strip()

            if not new_title:
                print("Task title cannot be empty.")
                continue

            if update_task(task_id, new_title):
                print("Task updated.")
            else:
                print("Task not found.")

        elif choice == "5":
            try:
                task_id = int(input("Enter task ID: "))
            except ValueError:
                print("ID must be a number.")
                continue

            if delete_task(task_id):
                print("Task deleted.")
            else:
                print("Task not found.")

        elif choice == "6":
            keyword = input("Enter keyword: ").strip()

            if not keyword:
                print("Keyword cannot be empty.")
                continue

            found_tasks = find_task(keyword)
            show_tasks(found_tasks)

        elif choice == "7":
            stats = get_tasks_stats()

            print(f'Total tasks: {stats["total"]}')

            if stats["by_status"]:
                print("By status:")

                for status, amount in stats["by_status"].items():
                    print(f"- {status}: {amount}")
            else:
                print("No tasks yet.")

        elif choice == "8":
            status = input("Enter status: ").strip()

            if not status:
                print("Status cannot be empty.")
                continue

            tasks_by_status = get_tasks_by_status(status)
            show_tasks(tasks_by_status)

        elif choice == "9":
            status = input("Enter status to delete: ").strip()

            if not status:
                print("Status cannot be empty.")
                continue

            deleted_count = delete_tasks_by_status(status)
            print(f"Deleted tasks: {deleted_count}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()