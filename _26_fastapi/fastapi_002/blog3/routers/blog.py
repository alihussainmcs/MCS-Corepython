from fastapi import APIRouter, Depends, HTTPException, status
from _26_fastapi.fastapi_001.blog import schemas, database, models
from sqlalchemy.orm import Session
from typing import List
from _26_fastapi.fastapi_001.blog.repository import blog

router = APIRouter(prefix='/blog', tags=['Blogs'])


@router.get('/', response_model=List[schemas.ShowBlog])
def retrieve_all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.post('/', status_code=201)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(database.get_db)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_id(id, db: Session = Depends(database.get_db)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, db: Session = Depends(database.get_db)):
    return blog.update(id, db)
