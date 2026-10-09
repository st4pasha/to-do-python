from fastapi import FastAPI
from app.repositories.tasks import tasks
from app.models.create_task_class import Task_to_create
from app.models.task_class import Task
from app.models.change_task_class import Update_task
from uuid import uuid4

app = FastAPI()

@app.get("/tasks")
def get_all_tasks():
    return tasks

@app.post("/tasks", status_code=201)
def create_task(task_from_server: Task_to_create):

    task = Task(id=str(uuid4()), title=task_from_server.title, description=task_from_server.description, is_completed=False)
    tasks.append(task)

    return {f"New task: {task.title}, completed: {task.is_completed}"}

@app.delete("/tasks/{title}", status_code=204)
def delete_task(title: str):
    for task in tasks:
        if task.title == title:
            tasks.remove(task)
            return {f"Deleted task: {title}"}
    return {"Task not found"}

@app.patch("/tasks{title}")
def change_task(task_change: Update_task, title: str):
    for task in tasks:
        if task.title == title:
            if task_change.title != None:
                task.title = task_change.title
            if task_change.description != None:
                task.description = task_change.description
            if task_change.is_completed != None:
                task.is_completed = task_change.is_completed
            return {f"New task: {task.title}, description: {task.description}, is_completed: {task.is_completed}"}
    return {"Task not found"}



