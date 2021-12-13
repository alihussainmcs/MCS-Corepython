from datetime import datetime
from typing import Optional

from pydantic import BaseModel

"""
main --> models class routes database
"""


class TaskBase(BaseModel):
    content: str
    description: Optional[str] = None


# schemas.TaskBase
class TaskCreate(TaskBase):
    description: str

    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

# TaskBase  --> BaseMoel  --> pyantic
# TaskCreate -> TaskBase
# Task  ------> TaskBase
