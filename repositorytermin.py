from schema import Zauzet_termin
import datetime
from model import Zauzet_termin as TerminModel
from model import Frizer as FrizerModel
from fastapi_sqlalchemy import db
from fastapi import HTTPException, status


def find_by_id(termin):
    db.session.query(TerminModel).filter(
        TerminModel.id == termin.id).first()

def get_all():
    zauzeti_termini=db.session.query(TerminModel).all()
    return zauzeti_termini

def create(termin:Zauzet_termin):
    zauzet_termin=TerminModel(**termin.dict())
    termin_exists= find_by_id(zauzet_termin)
    if termin_exists.id != zauzet_termin.frizer_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Termin nije zauzet")
    db.session.add(zauzet_termin)
    db.session.commit()
    db.session.refresh(zauzet_termin)
    return zauzet_termin

def delete_termin(termin:Zauzet_termin):
    za_brisanje = TerminModel(**termin.dict())
    termin_exists= find_by_id(za_brisanje)
    if termin_exists.id != za_brisanje.frizer_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Frizer ne postoji")
    db.session.delete(za_brisanje)
    db.session.commit()
    return za_brisanje