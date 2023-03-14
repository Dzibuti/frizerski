from fastapi import FastAPI
from schema import Frizer, Zauzet_termin, FrizerInDB, TerminInDB
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

@app.delete("/frizeri/{frizer_id}/")
async def delete_frizer(frizer_id: int) -> FrizerInDB:
        return service.delete_frizer(frizer_id=frizer_id)


@app.patch("/frizeri/{frizer_id}/")
async def patch(frizer: FrizerInDB) -> FrizerInDB:
    return service.patch(frizer=frizer)
    
@app.put("/frizeri/")
async def put_frizer (frizer:FrizerInDB) -> FrizerInDB:
    return service.put_frizer(frizer=frizer)

@app.get("/frizeri/{frizer_id}/")
async def root(frizer_id: int):
    print(frizer_id)
    return frizer_id

@app.delete("/frizeri/{frizer_id}/termini/{termin_id}")
async def delete_termin(termin_id: int)-> TerminInDB:
    return service.delete_termin(termin_id=termin_id)

@app.post("/frizeri/{frizer_id}/termini")
async def create_termin (frizer_id: int, termin:Zauzet_termin) -> TerminInDB:
    return service.create_termin(termin=termin)
