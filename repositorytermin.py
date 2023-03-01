from schema import Zauzet_termin
import datetime
from model import Zauzet_termin as TerminModel
from fastapi_sqlalchemy import db




def get_all():
    zauzeti_termini=db.session.query(TerminModel).all()
    return zauzeti_termini