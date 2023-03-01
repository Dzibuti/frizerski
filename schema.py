from pydantic import BaseModel
import datetime




class Zauzet_termin (BaseModel):
    frizer_id: int
    datum: datetime.datetime

    class Config:
        orm_mode = True

class Frizer(BaseModel):
    name: str
    pocetak_radnog_vremena: datetime.datetime
    kraj_radnog_vremena: datetime.datetime
    zauzet_termin: list[Zauzet_termin] | list = []
    
    class Config:
        orm_mode = True
    
class FrizerInDB(Frizer):
    id: int
    









