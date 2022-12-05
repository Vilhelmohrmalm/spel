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
