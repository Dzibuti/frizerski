from fastapi import FastAPI
from schema import Frizer, Zauzet_termin, FrizerInDB
import service
from fastapi_sqlalchemy import DBSessionMiddleware
from database import DATABASE_URL

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)

@app.get("/frizeri/")
async def frizeri():
    return service.get_all()

@app.post("/frizeri/")
async def create_frizer (frizer:Frizer) -> FrizerInDB:
    return service.create_frizer(frizer=frizer)


@app.get("/frizeri/{frizer_id}/")
async def root(frizer_id: int):
    print(frizer_id)
    return frizer_id
