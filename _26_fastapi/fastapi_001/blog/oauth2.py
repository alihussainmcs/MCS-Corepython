from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from _26_fastapi.fastapi_001.blog import tokens

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return tokens.verify_token(token,credentials_exception)
