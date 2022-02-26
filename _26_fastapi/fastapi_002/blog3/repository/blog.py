from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from _26_fastapi.fastapi_001.blog import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    blog1 = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog1.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available.')

    blog1.delete()
    db.commit()
    return 'deletion done'


def update(id: int, db: Session):
    blog1 = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog1.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available.')

    blog1.update({'title': 'title updated'})
    db.commit()
    return 'updated'


def show(id: int, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available.')
    return blogs
