from fastapi import FastAPI, Depends, Response, status, HTTPException
import uvicorn
from _26_fastapi.fastapi_002.blog0 import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/post_blog', status_code=201)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/get_blog')
def retrieve1(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/get_blog/{id}')
def retrieve(id, response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Detail ': f'blog with id {id} is not available.'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available.')
        # comment this and uncomment above two lines to to do the same thing
    return blogs


@app.delete('/delete_post/{id}', status_code=status.HTTP_204_NO_CONTENT)
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


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available.')

    blog.update({'title':'title updated'})
    db.commit()
    return 'done'


if __name__ == '__main__':
    uvicorn.run(app='main:app')
