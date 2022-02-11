from database import insert_data
from utils import database_retrive,\
    database_retrive_one,database_update,database_delete,sub_update
def service_insert(new_user,db):
    return insert_data(new_user,db)


def service_retrive(db):
    return database_retrive(db)

def service_retrive_one(id,db):
    return database_retrive_one(id,db)



def service_update(id,kannada,English,Hindhi,Maths,Science,Social,status,chance,db):
    return database_update(id,kannada,English,Hindhi,Maths,Science,Social,status,chance,db)

def service_subject(id,kannada,English,Hindhi,Maths,Science,Social,db):
    return sub_update(id,kannada,English,Hindhi,Maths,Science,Social,db)


def service_delete(id,db):
    return database_delete(id,db)