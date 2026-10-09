from pydantic import BaseModel

class Task(BaseModel):
    id: str
    title: str
    description: str
    is_completed: bool