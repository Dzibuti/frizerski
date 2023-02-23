from fastapi import FastAPI
from schema import datetime_format9, datetime_format20
from service import get_all

app = FastAPI()

@app.get("/frizeri/")
async def frizeri():
    print(get_all)
    return get_all()


@app.get("/frizeri/{frizer_id}/")
async def root(frizer_id: int):
    print(frizer_id)
    return frizer_id
