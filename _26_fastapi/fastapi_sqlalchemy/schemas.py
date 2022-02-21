from pydantic import BaseModel


class Employee(BaseModel):
    ename: str
    eid: int
    eloc: str


class EmployeeResponse(BaseModel):
    ename: str
    eid: int

    class Config:
        orm_mode = True
