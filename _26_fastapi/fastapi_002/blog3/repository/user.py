from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from _26_fastapi.fastapi_001.blog import models, schemas, database
from _26_fastapi.fastapi_001.blog.hashing import Hash


def create(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} is not available.')
    return user

