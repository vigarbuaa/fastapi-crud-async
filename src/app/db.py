import os
import uuid
from peewee import *
from enum import Enum
database = MySQLDatabase('stock', **{'charset': 'utf8', 'use_unicode': True, 'host': 'localhost', 'user': 'root', 'password': 'root'})

class Driver(Enum):
    SQLITE = "sqlite"
    MYSQL = "mysql"
    POSTGRESQL = "postgresql"
    # MONGODB = "mongodb"


def init(driver: Driver, settings: dict):
    init_funcs = {
        Driver.SQLITE: init_sqlite,
        Driver.MYSQL: init_mysql,
        Driver.POSTGRESQL: init_postgresql,
    }
    assert driver in init_funcs

    db = init_funcs[driver](settings)
    # bar, tick = init_models(db, driver)
    # return SqlManager(bar, tick)
    return db


def init_sqlite(settings: dict):
    database = settings["database"]
    path = str(get_file_path(database))
    db = SqliteDatabase(path)
    return db


def init_mysql(settings: dict):
    keys = {"database", "user", "password", "host", "port"}
    settings = {k: v for k, v in settings.items() if k in keys}
    db = MySQLDatabase(**settings)
    return db


def init_postgresql(settings: dict):
    keys = {"database", "user", "password", "host", "port"}
    settings = {k: v for k, v in settings.items() if k in keys}
    db = PostgresqlDatabase(**settings)
    return db

class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database

class Notes(BaseModel):
    id = CharField(column_name='id', primary_key=True)
    title = CharField(column_name='title')
    description = CharField(column_name='description')
    created_date = DateTimeField(column_name="created_date")

    class Meta:
        table_name = 'notes'

# add test code to create table
database.create_tables([Notes])
payload={
    "title":"hello",
    "description":"hello  world"
}
# add test code to insert data
query = Notes.create(
    id=uuid.uuid1(),
    title=payload["title"],
    description=payload["description"]
)