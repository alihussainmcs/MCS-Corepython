
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import models as db
import schemas as ss

app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.get('/')
def home():
    return {'Data': 'Home Page'}


@app.post('/token')
def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username, 'token_type': 'bearer'}


@app.get('/allowed')
def allowed_page(token: str = Depends(oauth_scheme)):
    return {'status': 'user logen in', 'username': token}


@app.post('/add_article')
def add_article(form_data: ss.Article_check):
    new_article = db.Article(title=form_data.title, body=form_data.body)
    db.session.add(new_article)
    db.session.commit()
    return {'status': 'success', 'id': new_article.identity}


@app.put('/update_data/{i}')
def update_data(form_data: ss.Article_check, i: int):
    query = db.session.query(db.Article).filter(db.Article.identity == i).first()
    query.title = form_data.title
    query.body = form_data.body
    db.session.commit()
    return {'status': 'changed'}


if __name__ == '__main__':
    uvicorn.run(app='main:app')

