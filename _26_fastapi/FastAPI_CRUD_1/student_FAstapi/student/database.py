from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgress123@127.0.0.1:5432/postgres"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def insert_data(new_user,db):
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return f'Data inserted successfully ,your student id is {new_user.stu_id} and result {new_user.status}'

