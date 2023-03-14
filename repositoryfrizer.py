from schema import Frizer, FrizerInDB
from fastapi_sqlalchemy import db
from model import Frizer as FrizerModel
from fastapi import HTTPException, status

def find_by_id(frizer):
    db.session.query(FrizerModel).filter(
        FrizerModel.id == frizer.id).first()

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
    nadjen_frizer = find_by_id(novi_frizer=novi_frizer)
    if nadjen_frizer.id == novi_frizer.id:
        db.session.query(FrizerModel).update(
            {"name":novi_frizer.name, 
             "pocetak_radnog_vremena": novi_frizer.pocetak_radnog_vremena,
             "kraj_radnog_vremena": novi_frizer.kraj_radnog_vremena})
        return
    return novi_frizer
    

def patch(frizer:Frizer):
    frizer=FrizerModel(**frizer.dict())
    nadjen_frizer=find_by_id(frizer=frizer)
    if nadjen_frizer != frizer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Frizer ne postoji")
    db.session.query.update({"pocetak_radnog_vremena": frizer.pocetak_radnog_vremena,
             "kraj_radnog_vremena": frizer.kraj_radnog_vremena})


def delete_frizer(frizer:Frizer):
    frizer_za_brisanje=FrizerModel(**frizer.dict())
    pronandjen_frizer = find_by_id(frizer_za_brisanje=frizer_za_brisanje)
    if frizer_za_brisanje != pronandjen_frizer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Frizer ne postoji")
    db.session.delete(frizer_za_brisanje)
    db.session.commit()
    return frizer_za_brisanje