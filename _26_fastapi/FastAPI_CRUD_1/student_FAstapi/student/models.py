from database import Base
from sqlalchemy import Column, Integer, String


class Student_model(Base):
    __tablename__ = 'student_data'
    stu_id = Column(Integer,primary_key=True)
    name = Column(String)
    Kannada = Column(Integer)
    English = Column(Integer)
    Hindhi = Column(Integer)
    Maths = Column(Integer)
    Science = Column(Integer)
    Social = Column(Integer)
    status=Column(String)
    chance=Column(String)

