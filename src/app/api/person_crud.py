from app.api.models import PersonSchema
from app.db import person, database


async def post(payload: PersonSchema):
    query = person.insert().values(
        idcard= payload.idcard,
        name= payload.name,
        address= payload.address,
        hometown=payload.hometown)
    return await database.execute(query=query)


async def get(id: int):
    query = person.select().where(id == person.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = person.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: PersonSchema):
    query = (
        person
        .update()
        .where(id == person.c.id)
        .values(title=payload.title, description=payload.description)
        .returning(person.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = person.delete().where(id == person.c.id)
    return await database.execute(query=query)
