from sqlalchemy import create_engine, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:12345@127.0.0.1:5432/postgres"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

Base = declarative_base()


class Article(Base):
    __tablename__ = 'Article'
    identity = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    body = Column(Text)

# Base.metadata.create_all(engine)
