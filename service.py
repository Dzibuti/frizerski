import repositoryfrizer
import repositorytermin
import model
from schema import Frizer, Zauzet_termin, FrizerInDB


def get_all():
    return repositoryfrizer.get_all()

def create_frizer(frizer: Frizer):
    return repositoryfrizer.create(frizer=frizer)

def put_frizer (frizer:FrizerInDB):
    return repositoryfrizer.put(frizer=frizer)

def delete_frizer(frizer_id: int):
    return repositoryfrizer.delete_frizer(frizer_id=frizer_id)

def patch (frizer:FrizerInDB):
    return repositoryfrizer.patch(frizer=frizer)

def get_all_termin():
    return repositorytermin.get_all()

def create_termin(frizer_id :int, termin: Zauzet_termin):
    return repositorytermin.create(frizer_id, termin=termin)

def delete_termin(termin_id: int):
    return repositorytermin.delete_termin(termin_id=termin_id)

