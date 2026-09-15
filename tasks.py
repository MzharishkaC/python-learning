tasks = []
def add_task(title :str) -> None :
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
print(get_tasks())
def get_completed_tasks() ->list :
    completed_task = []
    for task in tasks:
        if task["completed"] :
            completed_task.append(task)
    return completed_task
def complete_task(task_id: int) -> bool:
    for task in tasks  :
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
def update_task(task_id: int, new_title: str) ->bool:
    for task in tasks :
        if task["id"] == task_id :
            task["title"] = new_title
            return True
    return False
def clear_completed_task() ->int:
    completed_task = 0
    complete_task = tasks.copy()
    for task in complete_task:
        if task["completed"] :
            tasks.remove(task)
            completed_task += 1
    return completed_task
def get_pending_tasks() -> list:
    pending_tasks =[]
    for task in tasks:
        if task["completed"] == False:
            pending_tasks.append(task)
    return pending_tasks
def get_task_by_id(task_id : int) -> dict |None:
    for task in tasks :
        if task["id"] == task_id:
            return task
    return None
def count_complete_task() ->int:
    count = 0
    for task in tasks :
        if task["completed"]:
            count += 1
    return count




