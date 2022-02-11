from database import SessionLocal
import models
from models import Student_model
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def database_retrive(db):
    user_data = db.query(models.Student_model).filter(Student_model.stu_id >= 1)
    response = {}
    out_res = []
    for each in user_data:
        response['name'] = each.name
        response['result'] = each.status
    return response

def database_retrive_one(id,db):
    user_data = db.query(Student_model).filter(Student_model.stu_id == id).first()
    response = {}
    response['name'] = user_data.name
    response['result'] = user_data.status
    return response

def database_update(id,kannada,English,Hindhi,Maths,Science,Social,status,chance,db):
    update_obj = db.query(Student_model).filter(Student_model.stu_id == id).first()

    update_obj.chance=chance
    update_obj.stud_id=id
    update_obj.Kannada =kannada
    update_obj.English = English
    update_obj.Hindhi = Hindhi
    update_obj.Maths = Maths
    update_obj.Science = Science
    update_obj.Social = Social
    update_obj.status=status
    db.add(update_obj)
    db.commit()
    db.refresh(update_obj)
    return "data updated successfully"

def sub_update(id,kannada,English,Hindhi,Maths,Science,Social,db):

    update_sub = db.query(Student_model).filter(Student_model.stu_id == id).first()
    if kannada>0:
        update_sub.Kannada=kannada
    else:
        update_sub.Kannada = update_sub.Kannada
    if English > 0:
        update_sub.English = English
    else:
        update_sub.English = update_sub.English
    if Hindhi > 0:
        update_sub.Hindhi = Hindhi

    if Maths > 0:
        update_sub.Maths = Maths

    if Science > 0:
        update_sub.Science = Science

    if Social > 0:
        update_sub.Social = Science
    total = update_sub.Social+update_sub.Science+update_sub.Hindhi+update_sub.Kannada+update_sub.English+update_sub.Maths
    average = (total / 6)
    print(average)
    chance=update_sub.chance
    if average > 90:
        status = 'distiction'
        if status =='average':
            chance='no'
    elif average > 75 and average < 90:
        status = 'average'
        if status =='average':
            chance='no'
    elif average < 75:
        status = 'fail'


    update_sub.status=status
    update_sub.chance=chance
    db.add(update_sub)
    db.commit()
    db.refresh(update_sub)
    return f'Data updated successfully ,your student id is {update_sub.stu_id} and result {update_sub.status}'

def database_delete(id,db):
    if db.query(Student_model).filter(Student_model.stu_id == id).delete():
        db.commit()
        return "success"
    else:
        return 'user not found'