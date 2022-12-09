from spelfunktion import *
from vapen import *


def kista(Spelar_stats):
    inehåll = random.randint(1, 5)
    if inehåll == 1:
        print(Svärd)
    elif inehåll == 2:
        print(Sköld)
    elif inehåll == 3:
        print(Yxa)
    elif inehåll == 4:
        print(Pilbåge)
    elif inehåll == 5:
        print(Spjut)


kista()


def rum_typ():
    typ = random.randint(1, 10)
    if typ == 1 or typ == 2 or typ == 3 or typ == 4:
        fight()
    elif typ == 5 or typ == 6 or typ == 7 or typ == 8:
        val_vanlig()
    elif typ == 9:
        val_kista()
    elif typ == 10:
        fälla()
