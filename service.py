import repositoryfrizer
import repositorytermin

def get_all():
    frizeri = repositoryfrizer.get_all()
    zauzeti_termini = repositorytermin.get_all()
    for zauzet_termin in zauzeti_termini:
        for frizer in frizeri:
            if frizer.id == zauzet_termin.frizer_id:
                frizer.zauzet_termin.append(zauzet_termin.datum)
    return frizeri



#def post_termini ():
