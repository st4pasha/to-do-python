from app.database.create_connection import get_connection
from app.models.task_class import Task
from app.models.change_task_class import Update_task
import sqlite3

def add_info(task: Task, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.execute("""INSERT INTO Tasks(id, title, description, is_completed) VALUES(
    ?, ?, ?, ?)""", (task.id, task.title, task.description, 0))

    conn.commit()
    conn.close()
def get_task(conn: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.execute("SELECT * FROM Tasks")
    all_tasks = cursor.fetchall()
    conn.commit()
    conn.close()

    return all_tasks

def delete_task(id: str, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.execute("DELETE FROM Tasks WHERE id = ?;", (id,))
    conn.commit()
    conn.close()

def update_task(task_update: Update_task, id: str, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
    if task_update.is_completed != None:
        if task_update.is_completed == True:
            cursor.execute("""UPDATE Tasks
            SET is_completed = ?
            WHERE id = ?""", (1, id))
        else:
            cursor.execute("""UPDATE Tasks
                        SET is_completed = ?
                        WHERE id = ?""", (0, id))
    if task_update.description != None:
        cursor.execute("""UPDATE Tasks
        SET description = ?
        WHERE id = ?""", (task_update.description, id))
    if task_update.title != None:
        cursor.execute("""UPDATE Tasks
        SET title = ?
        WHERE id = ?""", (task_update.title, id))
    conn.commit()
    conn.close()

