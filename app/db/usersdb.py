import sqlalchemy

from db.db import DATABASE_URL

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_name", sqlalchemy.String),
    sqlalchemy.Column("password_hash", sqlalchemy.LargeBinary),
    sqlalchemy.Column("created_on", sqlalchemy.DateTime),
    sqlalchemy.Column("last_changed_on", sqlalchemy.DateTime),
    sqlalchemy.Column("last_login", sqlalchemy.DateTime),
    sqlalchemy.Column("is_admin", sqlalchemy.Boolean, default=False),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
