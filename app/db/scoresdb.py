import sqlalchemy
from sqlalchemy import ForeignKey
from db.usersdb import users

from db.db import DATABASE_URL

metadata = sqlalchemy.MetaData()

scores = sqlalchemy.Table(
    "scores",
    metadata,
    sqlalchemy.Column("score_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, ForeignKey(users.c.user_id), nullable=False),
    sqlalchemy.Column("score", sqlalchemy.Float),
    sqlalchemy.Column("submission_time", sqlalchemy.DateTime),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
