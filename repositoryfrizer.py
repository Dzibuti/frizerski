from schema import Frizer, FrizerInDB
from fastapi_sqlalchemy import db
from model import Frizer as FrizerModel
from fastapi import HTTPException, status

def get_all():
    frizeri=db.session.query(FrizerModel).all()
    return frizeri

def create(frizer:Frizer):
    dodat_frizer=FrizerModel(**frizer.dict())
    db.session.add(dodat_frizer)
    db.session.commit()
    db.session.refresh(dodat_frizer)
    return dodat_frizer

def put(frizer:FrizerInDB):
    novi_frizer=FrizerModel(**frizer.dict())
    nadjen_frizer = db.session.query(FrizerModel).filter(
        FrizerModel.id == novi_frizer.id).first()
    if nadjen_frizer.id == novi_frizer.id:
        db.session.query(FrizerModel).update({novi_frizer.name, novi_frizer.pocetak_radnog_vremena,
                                              novi_frizer.kraj_radnog_vremena})
        return
    return novi_frizer
    

def patch(frizer:Frizer):
    pass

def delete_frizer(frizer:Frizer.id):
    za_brisanje = db.session.query(FrizerModel).filter(
        FrizerModel.id == za_brisanje).first()
    if not za_brisanje:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Frizer ne postoji")
    db.session.delete(za_brisanje)
    db.session.commit()
    return za_brisanje