from database import Base
from sqlalchemy import Column, Integer, String


class Employee_model(Base):
    __tablename__ = 'ali_employee'
    eid = Column(Integer, primary_key=True)
    ename = Column(String)
    eloc = Column(String)
