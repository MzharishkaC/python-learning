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
print(tasks)
def get_tasks() -> list:
    return tasks
print(get_tasks())
def get_completed_tasks() ->list :
    completed_task = []
    for task in tasks:
        if task["completed"] :
            completed_task.append(task)
    return completed_task
print(get_completed_tasks())