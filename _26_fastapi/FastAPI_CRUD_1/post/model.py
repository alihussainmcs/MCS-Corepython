import sqlalchemy
from _26_fastapi.FastAPI_CRUD_1.config import metadata
from datetime import datetime

''' SQLAlchemy Model'''
posts = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(100), unique=True),
    sqlalchemy.Column("body", sqlalchemy.Text),
    sqlalchemy.Column("is_published", sqlalchemy.Boolean),
    sqlalchemy.Column("created", sqlalchemy.DateTime, default=datetime.utcnow().strftime("%Y-%m-%d" "%H:%M:%S")),
    sqlalchemy.Column("modified", sqlalchemy.DateTime, default=datetime.utcnow().strftime("%Y-%m-%d" "%H:%M:%S"))
)
