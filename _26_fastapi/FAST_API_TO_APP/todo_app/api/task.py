from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..dependencies import get_db

# app = Fastapi()
router = APIRouter(prefix="/api")


# 127.0.0.1/api/tasks
# @app.get('/tasks', response_moel = )
# request boy--> from front en response boy --> we wil sen to front en
@router.get('/tasks', response_model=List[schemas.Task])
def get_items(db: Session = Depends(get_db)):
    """
    item : Item
    item = Item
        Return all task in database
    """
    items = utils.get_tasks(db)
    return items


# 127.0.0.1/api/tasks/12

"""
i 1 2 3 4 5 6 
6
"""


# fb.com/Harsha
# fb.com/ranjith
@router.get('/tasks/{task_id}', response_model=schemas.Task)
def get_item_by_id(task_id: int, db: Session = Depends(get_db)):
    db_task = utils.get_tasks_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_task


@router.post('/create-task/', response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)) -> schemas.Task:
    """                                                                   -> str
                                                                          -> int

    Payload --> CONTENT : String
                ESCRIPTION : String

                SCHEMAS.TaskCreate --> content is string or not
                                    -> escription is string or not
                task : schemastask: schemas.TaskCreate.TaskCreate
                task = {content :str ,escription : str}
        Create a task in database
            - task: TaskCreate Schema
        Return The Task Created
    """
    return utils.create_task(db, task=task)
    # return str


@router.put("/update_task/{task_id}")
def update_task(task_id: int, done: bool, db: Session = Depends(get_db)):
    db_todo = utils.update_task(db, task_id, done)
    return db_todo


@router.delete("/delete_task/{task_id}")
def delete_task(task_id: int, done: bool, db: Session = Depends(get_db)):
    db_todo = utils.delete_task(db, task_id, done)
    return db_todo
