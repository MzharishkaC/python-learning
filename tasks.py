tasks = []


def add_task(title: str) -> dict:
    new_id = len(tasks) + 1
    new_dict = {
        "id": new_id,
        "title": title,
        "status": "pending"
    }
    tasks.append(new_dict)
    return new_dict


def get_tasks() -> list:
    return tasks


def delete_task(task_id: int) -> bool:
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return True
    return False


def update_task(task_id: int, new_title: str) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            return True
    return False


def get_task_by_id(task_id: int) -> dict | None:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def find_task(keyword: str) -> list:
    found_task = []
    for task in tasks:
        if keyword.lower() in task["title"].lower():
            found_task.append(task)
    return found_task


def get_tasks_by_status(status: str) -> list:
    task_status = []
    for task in tasks:
        if task["status"] == status:
            task_status.append(task)
    return task_status


def change_task_status(task_id: int, status: str) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            return True
    return False


def get_tasks_amount_by_status(status: str) -> int:
    count = 0
    for task in tasks:
        if task["status"] == status:
            count += 1
    return count


def get_tasks_stats() -> dict:
    stats = {
        "total": len(tasks),
        "by_status": {}
    }

    for task in tasks:
        status = task["status"]

        if status not in stats["by_status"]:
            stats["by_status"][status] = 0

        stats["by_status"][status] += 1

    return stats


def delete_tasks_by_status(status: str) -> int:
    count = 0
    deleted_tasks = tasks.copy()
    for task in deleted_tasks:
        if task["status"] == status:
            tasks.remove(task)
            count += 1
    return count
