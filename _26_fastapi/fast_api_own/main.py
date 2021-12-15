# main.py
# Import FastAPI
from fastapi import FastAPI
import uvicorn
import api

# Initialize the app
app = FastAPI()

app.include_router(api.router)


# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to Ali's Technical Blog"}


if __name__ == "__main__":
    uvicorn.run(app='main:app')
