from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped
from database import Base
import datetime

class Frizer (Base):
    __tablename__ = "frizeri"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=False, index=True)
    pocetak_radnog_vremena=Column(DateTime)
    kraj_radnog_vremena=Column(DateTime)
    zauzet_termini= relationship(
        "Zauzet_termin",
        uselist=True,
        lazy="selectin"
    )

class Zauzet_termin(Base):
    __tablename__ = "zauzeti_termini"

    id =Column(Integer, primary_key=True, index=True)
    frizer_id=Column(Integer, ForeignKey("frizeri.id"))
    datum=Column(DateTime)

    

