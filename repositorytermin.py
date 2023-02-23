from schema import Zauzet_termin
import datetime
from repositoryfrizer import frizer1
datetime_format9 = datetime.datetime(2023, 2, 23, 9, 00)
termin1 = Zauzet_termin(frizer_id=frizer1.id, datum=datetime_format9)

def get_all():
    return [termin1]