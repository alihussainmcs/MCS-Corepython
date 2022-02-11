from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name    :str
    Kannada :int
    English :int
    Hindhi  :int
    Maths   :int
    Science :int
    Social  :int

class Student_update(BaseModel):
    id:int
    Kannada :Optional[int]=None
    English :Optional[int]=None
    Hindhi  :Optional[int]=None
    Maths   :Optional[int]=None
    Science :Optional[int]=None
    Social  :Optional[int]=None

