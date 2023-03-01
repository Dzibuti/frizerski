from schema import Frizer, FrizerInDB
from fastapi_sqlalchemy import db
from model import Frizer as FrizerModel
from fastapi import HTTPException, status







def get_all():
    frizeri=db.session.query(FrizerModel).all()
    return frizeri

def create(frizer:Frizer):
    dodat_frizer=FrizerModel(**frizer.dict())
    frizer_exists= db.session.query(FrizerModel).filter(
        FrizerModel.name == dodat_frizer.name).first()
    if frizer_exists != None:
        print ("Frizer vec postoji")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Frizer postoji")
    db.session.add(dodat_frizer)
    db.session.commit()
    db.session.refresh(dodat_frizer)
    return dodat_frizer
