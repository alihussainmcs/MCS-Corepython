import uvicorn
from fastapi import FastAPI
from _26_fastapi.fastapi_course.blog import models
from _26_fastapi.fastapi_course.blog.database import engine
from _26_fastapi.fastapi_course.blog.routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

if __name__ == '__main__':
    uvicorn.run(app='main:app')
