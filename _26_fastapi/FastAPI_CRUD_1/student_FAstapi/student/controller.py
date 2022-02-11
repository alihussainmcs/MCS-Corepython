from fastapi import FastAPI, Depends
import uvicorn
from schemas import Student,Student_update
from sqlalchemy.orm import Session
from utils import get_db
from service import service_insert, service_retrive, \
    service_retrive_one, service_update,service_delete,service_subject
import models
from database import engine
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

@app.post('/insert',status_code=201 )
def insert_data(std : Student, db : Session = Depends(get_db)):
    print(std.Kannada)
    total=std.Kannada+std.English+std.Hindhi+std.Maths+std.Science+std.Social
    average=(total/6)
    print(average)
    if average>90:
       status='distiction'
    elif average>75 and average<90:
        status='average'
    elif average<75:
        status='fail'

    if status =='fail':
        chance = 'yes'
    else:
        chance='no'

    new_user = models.Student_model(name=std.name,Kannada=std.Kannada,English=std.English,Hindhi=std.Hindhi,
                                    Maths=std.Maths,Science=std.Science,Social=std.Social,status=status,chance=chance)

    return service_insert(new_user,db)
'''
@app.get('/retrieve',status_code=200)
def retrieve_data(db : Session = Depends(get_db)):
    return service_retrive(db)
'''

@app.get('/retrieve/{id}',status_code=200)
def retrieve_data(id:int, db : Session = Depends(get_db)):
    return service_retrive_one(id,db)

@app.put('/update')
def update_data(emp : Student_update,db : Session = Depends(get_db)):

    total = emp.Kannada + emp.English + emp.Hindhi + emp.Maths + emp.Science + emp.Social
    average = (total / 6)
    print(average)
    if average > 90:
        status = 'distiction'
    elif average > 75 and average < 90:
        status = 'average'
    elif average < 75:
        status = 'fail'

    if status =='fail':
        chance = 'yes'
    else:
        chance='no'
    id=emp.id
    kannada = emp.Kannada
    English= emp.English
    Hindhi = emp.Hindhi
    Maths = emp.Kannada
    Science = emp.Science
    Social = emp.Social
    return service_update(id,kannada,English,Hindhi,Maths,Science,Social,status,chance,db)

@app.put('/sub')
def update_sub(sub:Student_update,db : Session = Depends(get_db)):
    id = sub.id
    kannada = sub.Kannada
    English = sub.English
    Hindhi = sub.Hindhi
    Maths = sub.Kannada
    Science = sub.Science
    Social = sub.Social
    return service_subject(id,kannada,English,Hindhi,Maths,Science,Social,db)


@app.delete('/delete/{id}')
def delete_data(id:int,db : Session = Depends(get_db)):
    return service_delete(id,db)


if __name__ == '__main__':
    uvicorn.run(app)