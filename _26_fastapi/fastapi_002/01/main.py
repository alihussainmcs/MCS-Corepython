from typing import Optional

from fastapi import FastAPI
import uvicorn

app = FastAPI()

"""
@app.get('/')
def index():
    return {'Data': 'blog list'}



@app.get('/blog')  # link will be like     http://127.0.0.1:8000/blog?limit=20                   20 or any number
def index(limit):
    return {'Data': f'{limit} blog from the db'}




@app.get('/blog')
def index(limit, published: bool):                              # Query parameters
    if published:                                               # http://127.0.0.1:8000/blog?limit=50&published=true
        return {'Data': f'{limit} published blog from the db'}
    else:                                                       # http://127.0.0.1:8000/blog?limit=50&published=false
        return {'Data': f'{limit} blog from the db'}
"""


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):    # http://127.0.0.1:8000/blog?sort=latest
    if published:                                               # http://127.0.0.1:8000/blog
        return {'Data': f'{limit} published blog from the db'}
    else:
        return {'Data': f'{limit} blog from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'Data': 'all unpublished blogs.'}


'''
Since we are doing dynamic routing so if we write unpublished below show method then it will give 
type error that's why we have write it above show and comments method
'''


@app.get('/blog/{id}')    # path parameter
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch blog with id = id
    return {'data': {id, 'some comments......'}}


if __name__ == '__main__':
    uvicorn.run(app='main:app')
