from database import SessionLocal
import models
from models import Employee_model


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def database_retrive(db):
    user_data = db.query(models.Employee_model).filter(Employee_model.eid >= 14)
    response = {}
    out_res = []
    for each in user_data:
        response['ename'] = each.ename
        response['eid'] = each.eid
        response['eloc'] = each.eloc
        out_res.append(response)
    return out_res


def database_retrive_one(id, db):
    user_data = db.query(Employee_model).filter(Employee_model.eid == id).first()
    response = {}
    response['ename'] = user_data.ename
    response['eid'] = user_data.eid
    response['eloc'] = user_data.eloc
    return response


def database_update(name, id, loc, db):
    update_obj = db.query(Employee_model).filter(Employee_model.eid == id).first()
    update_obj.ename = name
    update_obj.eloc = loc
    db.add(update_obj)
    db.commit()
    db.refresh(update_obj)
    return "data updated successfully"


def database_delete(id, db):
    if db.query(Employee_model).filter(Employee_model.eid == id).delete():
        db.commit()
        return "success"
    else:
        return 'user not found'
