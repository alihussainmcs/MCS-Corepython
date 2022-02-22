from fastapi import FastAPI
import uvicorn
from _26_fastapi.fastapi_001.blog import schemas, models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post('/blog')
def create(request: schemas.Blog):
    return request


if __name__ == '__main__':
    uvicorn.run(app='main:app')
