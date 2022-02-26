from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from _26_fastapi.fastapi_001.blog import schemas, database, models, tokens
from _26_fastapi.fastapi_001.blog.hashing import Hash
from fastapi.security import OAuth2PasswordBearer


router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request: OAuth2PasswordBearer = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credential')

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect Password')

    access_token = tokens.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
