from valfunktioner import *
from karaktär import *
from text_animering import *
from vapen import *
from fight import *


def karaktärsval():
    namn = int(typingInput("""
    Välj din karaktär.
    svara med 1, 2 eller 3.

    1. Assasin       2. Barbarian       3. Knight
    hp = 5           hp = 8             hp = 10 
    str = 10         str = 7            str = 5 
    """))

    if namn == 1:
        Spelar_stats = (Assasin)
        typingPrint(" Du är nu en Assasin med 5 hp och 10 str ")
        return (Spelar_stats)

    elif namn == 2:
        Spelar_stats = (Barb)
        typingPrint(" Du är nu en Barbarian med 8 hp och 7 str ")
        return (Spelar_stats)

    elif namn == 3:
        Spelar_stats = (Knight)
        typingPrint(" Du är nu en Knight med 10 hp och 5 str ")
        return (Spelar_stats)

    else:
        typingPrint("svara 1, 2 eller 3 din sopa")
        karaktärsval()


def main():
    typingPrint("""
    Välkommen till Daedalus labyrint

    Ditt mål är att ta dig genom labyrinten men se upp för Taurus.
    Han har en slimekapasitet på 100%.
    """)

    karaktärsval()

    val_vanlig(Spelar_stats)


main()
