from pydantic import BaseModel
import datetime
from typing import Union, List



class Zauzet_termin (BaseModel):
    frizer_id: int
    datum: datetime.datetime

    class Config:
        orm_mode = True

class TerminInDB (Zauzet_termin):
    id: int

class Frizer(BaseModel):
    name: str
    pocetak_radnog_vremena: datetime.datetime
    kraj_radnog_vremena: datetime.datetime
    zauzet_termini: List[Zauzet_termin] = []
    
    class Config:
        orm_mode = True
    
class FrizerInDB(Frizer):
    id: int

class GetAllFrizeriResponse(BaseModel):
    frizeri: List[
        FrizerInDB
    ]










