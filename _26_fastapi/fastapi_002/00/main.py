from fastapi import FastAPI
import uvicorn

app = FastAPI()  # instance of FastAPI


@app.get('/')  # base path  , @app -- path operation decorator
def name():  # path operation function
    return 'hey Ali'


@app.get('/name/')  # name path
def name():
    return {'Data': {'Name': 'ALI'}}


@app.get('/about/')  # get method and get is operation
def about():
    return {'about': {'about page'}}


@app.get('/about1/')
def about():
    return {'about': 'about page'}
    

if __name__ == '__main__':
    uvicorn.run(app='main:app')
