from schema import Frizer, FrizerInDB
from fastapi_sqlalchemy import db
from model import Frizer as FrizerModel
from fastapi import HTTPException, status

def find_by_id(frizer_id:int):
    frizer = db.session.query(FrizerModel).filter(
        FrizerModel.id == frizer_id).first()
    if frizer == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Frizer sa trazenim ID-ijem ({frizer_id}) ne postoji")
    return frizer
        
    

def get_all():
    frizeri=db.session.query(FrizerModel).all()
    return frizeri 

def create(frizer:Frizer):
    dodat_frizer=FrizerModel(**frizer.dict())
    db.session.add(dodat_frizer)
    db.session.commit()
    db.session.refresh(dodat_frizer)
    return dodat_frizer

def patch(frizer:FrizerInDB):
    nadjen_frizer = find_by_id(frizer.id)
    nadjen_frizer.pocetak_radnog_vremena = frizer.pocetak_radnog_vremena
    nadjen_frizer.kraj_radnog_vremena = frizer.kraj_radnog_vremena
    db.session.commit()
    return nadjen_frizer
    

def put(frizer:FrizerInDB):
    nadjen_frizer=find_by_id(frizer.id)
    db.session.query(FrizerModel).update({
             "name": nadjen_frizer.name,
             "pocetak_radnog_vremena": nadjen_frizer.pocetak_radnog_vremena,
             "kraj_radnog_vremena": nadjen_frizer.kraj_radnog_vremena})
    return nadjen_frizer


def delete_frizer(frizer_id:int):
    pronandjen_frizer = find_by_id(frizer_id=frizer_id)
    db.session.delete(pronandjen_frizer)
    db.session.commit()
    return pronandjen_frizer