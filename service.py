import repositoryfrizer
import repositorytermin
import model
from schema import Frizer


def get_all():
    return repositoryfrizer.get_all()

def create_frizer(frizer: Frizer):
    return repositoryfrizer.create(frizer=frizer)
