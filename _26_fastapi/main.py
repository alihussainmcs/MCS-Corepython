from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    number: int


@app.get('/')
def get():
    return 'Hello World'


@app.get('/home/{name}')
def get(name):
    return f'Hello {name}'


@app.post('/home/post/')
def post(game: Item):
    #  game --> Item --> game = {'name':'ali', 'number:12}
    new_name = game.name
    new_number = game.number
    return f'Hello {new_name} you are in {new_number}'


if __name__ == "__main__":
    uvicorn.run(app='main:app')

# Create Read Update Delete ---> Post Get Put Delete
"""
class Contact(BaseModel):
    contact_id: int
    name: str


@app.post('/contact')
async def create_contact(contact: Contact):
    return contact


@app.get("/")
def read_contact():
    return {"Hello": "World"}


@app.put("/contact/{id}")
def update_contact(id: int):
    return {"update contact item with id ": id}


@app.delete("/contact/{id}")
def delete_contact(id: int):
    return {"delete contact item with id ": id}

"""
