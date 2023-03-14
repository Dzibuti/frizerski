from schema import Zauzet_termin
import datetime
from model import Zauzet_termin as TerminModel
from model import Frizer as FrizerModel
from fastapi_sqlalchemy import db
from fastapi import HTTPException, status


def find_by_id(termin_id):
    termin = db.session.query(TerminModel).filter(
        TerminModel.id == termin_id).first()
    if termin == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Termin sa trazenim ID-ijem ({termin_id}) ne postoji")
    return termin

def get_all():
    zauzeti_termini=db.session.query(TerminModel).all()
    return zauzeti_termini

def create(termin:Zauzet_termin):
    dodat_termin= TerminModel(**termin.dict())
    db.session.add(dodat_termin)
    db.session.commit()
    db.session.refresh(dodat_termin)
    return dodat_termin

def delete_termin(termin_id:int):
    termin_delete= find_by_id(termin_id=termin_id)
    db.session.delete(termin_delete)
    db.session.commit()
    return termin_delete