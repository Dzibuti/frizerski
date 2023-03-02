import repositoryfrizer
import repositorytermin
import model
from schema import Frizer, Zauzet_termin


def get_all():
    return repositoryfrizer.get_all()

def create_frizer(frizer: Frizer):
    return repositoryfrizer.create(frizer=frizer)

def put_frizer (frizer:Frizer):
    # return repositoryfrizer.put(frizer=frizer)
    pass

def delete_frizer(frizer:Frizer):
    return repositoryfrizer.delete_frizer(frizer=frizer)

def get_all_termin():
    return repositorytermin.get_all()

def create_termin(termin: Zauzet_termin):
    return repositorytermin.create(termin=termin)

def delete_termin(termin:Zauzet_termin):
    return repositorytermin.delete_termin(termin=termin)

