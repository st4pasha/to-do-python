from fastapi import FastAPI
from app.repositories.tasks import tasks
from app.models.create_task_class import Task_to_create
from app.models.task_class import Task
from app.models.change_task_class import Update_task
from uuid import uuid4
from app.repositories.sqllite import add_info, get_connection, get_task, delete_task, update_task
from app.database.create_connection import create_table

create_table(*get_connection())

app = FastAPI()

@app.get("/tasks")
def get_all_tasks():
    return get_task(*get_connection())

@app.post("/tasks", status_code=201)
def create_task(task_from_server: Task_to_create):

    task = Task(id=str(uuid4()), title=task_from_server.title, description=task_from_server.description, is_completed=False)
    add_info(task, *get_connection())
    

    return {f"New task: {task.title}, completed: {task.is_completed}"}

@app.delete("/tasks/{id}", status_code=204)
def delete(id: str):
            delete_task(id, *get_connection())
            return "Task deleted"

@app.patch("/tasks/{id}")
def change_task(task_change: Update_task, id: str):
    update_task(task_change, id, *get_connection())