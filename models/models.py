import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON

metadate = MetaData()

roles = Table(
    "roles",
    metadate,
    Column("id", Integer, primary_key=True),  # primary_key=True - каждый id должен быть уникален
    Column("name", String, nullable=False),  # nullable=False -этот столбец не может быть пустым
    Column("permissions", JSON),
)

users = Table(
    "users",
    metadate,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
    Column("username", String, primary_key=True, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.UTC),
    Column("role", Integer, ForeignKey("roles.id")),
)