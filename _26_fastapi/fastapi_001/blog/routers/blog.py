from fastapi import APIRouter, Depends, HTTPException, status
from _26_fastapi.fastapi_001.blog import schemas, database, models
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix='/blog', tags=['Blogs'])


@router.get('/', response_model=List[schemas.ShowBlog])
def retrieve_all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/', status_code=201)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def retrieve(id, db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Detail ': f'blog with id {id} is not available.'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available.')
        # comment this and uncomment above two lines to to do the same thing
    return blogs


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_id(id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)  # .delete(synchronize_session=False)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available.')

    blog.delete()
    db.commit()
    return 'deletion done'


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available.')

    blog.update({'title': 'title updated'})
    db.commit()
    return 'done'
