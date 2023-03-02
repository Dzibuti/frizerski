from schema import Zauzet_termin
import datetime
from model import Zauzet_termin as TerminModel
from model import Frizer as FrizerModel
from fastapi_sqlalchemy import db
from fastapi import HTTPException, status




def get_all():
    zauzeti_termini=db.session.query(TerminModel).all()
    return zauzeti_termini

def create(termin:Zauzet_termin):
    zauzet_termin=TerminModel(**termin.dict())
    frizer_exists= db.session.query(FrizerModel).filter(
        FrizerModel.id == zauzet_termin.id).first()
    if frizer_exists.id != zauzet_termin.frizer_id:
        print ("Frizer ne postoji")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Frizer ne postoji")
    db.session.add(zauzet_termin)
    db.session.commit()
    db.session.refresh(zauzet_termin)
    return zauzet_termin

def delete_termin(termin:Zauzet_termin):
    za_brisanje = TerminModel(**termin.dict())
    termin_exists= db.session.query(TerminModel).filter(
        TerminModel.id == za_brisanje.id).first()
    if termin_exists.id != za_brisanje.frizer_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Frizer ne postoji")
    db.session.delete(za_brisanje)
    db.session.commit()
    return za_brisanje