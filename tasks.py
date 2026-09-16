tasks = []


def add_task(title: str) -> None:
    new_id = len(tasks) + 1
    new_dict = {
        "id": new_id,
        "title": title,
        "completed": False
    }
    tasks.append(new_dict)


add_task("Learn Git")
add_task("Learn Pythin Core")


def get_tasks() -> list:
    return tasks


def complete_task(task_id: int) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False


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


def clear_completed_task() -> int:
    completed_task = 0
    complete_task = tasks.copy()
    for task in complete_task:
        if task["completed"]:
            tasks.remove(task)
            completed_task += 1
    return completed_task


def get_task_by_id(task_id: int) -> dict | None:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def count_completed_task() -> int:
    count = 0
    for task in tasks:
        if task["completed"]:
            count += 1
    return count


def find_task_position(task_id: int) -> int:
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return index
    return -1


def toggle_task(task_id: int) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            return True
    return False


def get_incomplete_count() -> int:
    incomplete_task = 0
    for task in tasks:
        if not task["completed"]:
            incomplete_task += 1
    return incomplete_task


def get_tasks_by_status(completed: bool) -> list:
    task_status = []
    for task in tasks:
        if task["completed"] == completed:
            task_status.append(task)
    return task_status


def find_task(keyword: str) -> list:
    keyword_word = []
    for task in tasks:
        if keyword.lower() in task["title"].lower():
            keyword_word.append(task)
    return keyword_word


def get_tasks_stats() -> dict:
    total = len(tasks)
    completed = 0
    pending = 0

    for task in tasks:
        if task["completed"]:
            completed += 1
        else:
            pending += 1

    return {
        "total": total,
        "completed": completed,
        "pending": pending
    }


def sort_tasks_by_status() -> list:
    sorted_tasks = []
    for task in tasks:
        if task["completed"] == False:
            sorted_tasks.append(task)
    for task in tasks:
        if task["completed"]:
            sorted_tasks.append(task)
    return sorted_tasks


def get_tasks_by_status(status: str) -> list:
    task_status = []
    for task in tasks:
        if status == "completed" and task["completed"]:
            task_status.append(task)
        elif status == "pending" and not task["completed"]:
            task_status.append(task)
    return task_status

def change_task_status(task_id: int, status: str) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            if status == "completed":
                task["completed"] = True
            elif status == "pending":
                task["completed"] = False
            return True
    return False
# Working on status feature
