from sqlalchemy.orm import Session, exc
from . import models, schemas

"""crud.py utils.py"""
"""
1. get all tasks
2. get task by id 
3. create task --- i will save that to database
4. update task by id
5. delete task by id
"""


def get_tasks(db: Session):
    """ 
        Return All Task in Database 
    """
    # SELECT * FROM WHERE TASK
    return db.query(models.Task).all()


def get_tasks_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def create_task(db: Session, task: schemas.TaskCreate) -> schemas.Task:
    """
    contentd
    descr
        Create a Task in database
            - task: TaskCreate
    """
    task_data = models.Task(content=task.content, description=task.description)
    db.add(task_data)
    db.commit()
    db.refresh(task_data)
    return task_data


def update_task(db: Session, task_id: int, done: bool):
    """
            Update a Task in database
        """
    task_data = db.query(models.Task).filter(models.Task.id == task_id).first()
    task_data.done = done
    db.commit()
    db.refresh(task_data)
    return task_data


def delete_task(db: Session, task_id: int, done: bool):
    """
            Delete a Task in database
        """
    task_data = db.query(models.Task).filter(models.Task.id == task_id).delete()
    if not task_data:
        raise exc.NoResultFound
    return {'id': str(task_id)}
