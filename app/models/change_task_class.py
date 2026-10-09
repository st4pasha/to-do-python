from pydantic import BaseModel

class Update_task(BaseModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None