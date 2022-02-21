from fastapi import FastAPI, Depends
import uvicorn
from schemas import Employee, EmployeeResponse
from sqlalchemy.orm import Session
from utils import get_db
from service import service_insert, service_retrive, \
    service_retrive_one, service_update, service_delete
import models
from database import engine
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post('/insert', status_code=201)
def insert_data(emp: Employee, db: Session = Depends(get_db)):
    new_user = models.Employee_model(eid=emp.eid,
                                     ename=emp.ename, eloc=emp.eloc)

    return service_insert(new_user, db)


@app.get('/retrieve', status_code=200, response_model=List[EmployeeResponse])
def retrieve_data(db: Session = Depends(get_db)):
    return service_retrive(db)


@app.get('/retrieve/{id}', status_code=200, response_model=EmployeeResponse)
def retrieve_data(id: int, db: Session = Depends(get_db)):
    return service_retrive_one(id, db)


@app.put('/update')
def update_data(emp: Employee, db: Session = Depends(get_db)):
    name = emp.ename
    id = emp.eid
    loc = emp.eloc
    return service_update(name, id, loc, db)


@app.delete('/delete/{id}')
def delete_data(id: int, db: Session = Depends(get_db)):
    return service_delete(id, db)


if __name__ == "__main__":
    uvicorn.run(app='controller:app')
