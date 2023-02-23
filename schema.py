from pydantic import BaseModel
import datetime
import time

datetime_format9 = datetime.datetime(2023, 2, 23, 9, 00)

datetime_format20 = datetime.datetime(2023, 2, 23, 20, 00)


class Zauzet_termin (BaseModel):
    frizer_id: int
    datum: datetime.datetime

    
class Frizer(BaseModel):
    id: int
    name: str
    pocetak_radnog_vremna = datetime_format9
    kraj_radnog_vremna = datetime_format20
    zauzet_termin: list[Zauzet_termin] | list = []
    
# class Termin (BaseModel):
#     id: int
#     datum: int
#     #Ako smena ide u backu
#     #smena: bool
#     #U endpointu napraviti if petlju koja na false boolean lista prepodnevne
#     #a na true bolean popodnevne termine
#     sat = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30'
#     '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30'
#     '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00']









