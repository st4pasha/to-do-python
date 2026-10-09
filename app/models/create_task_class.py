from pydantic import BaseModel

class Task_to_create(BaseModel):
    title: str
    description: str