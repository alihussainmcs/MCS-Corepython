from fastapi import FastAPI
import uvicorn
from _26_fastapi.fastapi_001.blog import models
from database import engine

from routers import blog, user

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(blog.router)

app.include_router(user.router)


if __name__ == '__main__':
    uvicorn.run(app='main:app')
