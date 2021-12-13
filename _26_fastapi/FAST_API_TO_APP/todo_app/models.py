from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy.orm import relationship


# yanamo63
# Create Model
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    description = Column(String)

# tasks
# i content description
# 1 harsha taking class
# content -- title -- need to go luch des--> what i woould like to eat

#
# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#
#     items = relationship("Item", back_populates="owner")
#
#
# class Item(Base):
#     __tablename__ = "items"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#
#     owner = relationship("User", back_populates="items")
