from fastapi import APIRouter, Depends, HTTPException, status
from _26_fastapi.fastapi_001.blog.repository import user

from _26_fastapi.fastapi_001.blog import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix='/user',
                   tags=['Users'])


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request,db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)
