from pydantic import BaseModel


class Article_check(BaseModel):
    title: str
    body: str
