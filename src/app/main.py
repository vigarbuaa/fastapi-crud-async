from fastapi import FastAPI
from app.api import notes, ping
#from app.db import database, engine, metadata
from app.db import database

# metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    #await database.connect()
    print("web server startup!!!")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
