from fastapi import FastAPI, Depends, Response, status, HTTPException
import uvicorn
from _26_fastapi.fastapi_002.blog2 import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from _26_fastapi.fastapi_001.blog.hashing import Hash
app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/post_blog', status_code=201, tags=['Blogs'])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/get_blog', response_model=List[schemas.ShowBlog], tags=['Blogs'])
def retrieve_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/get_blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['Blogs'])
def retrieve(id, response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Detail ': f'blog with id {id} is not available.'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available.')
        # comment this and uncomment above two lines to to do the same thing
    return blogs


@app.delete('/delete_post/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
def destroy_id(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)  # .delete(synchronize_session=False)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available.')

    blog.delete()
    db.commit()
    return 'deletion done'


"""
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).update({'title':'title updated'})
    db.commit()
    return 'done'
"""


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available.')

    blog.update({'title': 'title updated'})
    db.commit()
    return 'done'


@app.post('/user', response_model=schemas.ShowUser, tags=['Users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request


@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['Users'])
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} is not available.')
    return user


if __name__ == '__main__':
    uvicorn.run(app='main:app')
