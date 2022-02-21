from database import insert_data
from utils import database_retrive, \
    database_retrive_one, database_update, database_delete


def service_insert(new_user, db):
    if new_user.eid % 2 == 0:
        return insert_data(new_user, db)
    else:
        return "Fail"


def service_retrive(db):
    return database_retrive(db)


def service_retrive_one(id, db):
    if id > 10:
        return database_retrive_one(id, db)
    else:
        return "user is not available"


def service_update(name, id, loc, db):
    if id % 2 == 0:
        return database_update(name, id, loc, db)
    else:
        return "user is not allowed to update"


def service_delete(id, db):
    return database_delete(id, db)
