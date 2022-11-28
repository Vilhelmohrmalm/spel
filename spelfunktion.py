from valfunktioner import *
from Karaktärer import *



def karaktärsval():
    namn=int(input("""
    Välj din karaktär.
    svara med 1, 2 eller 3.

    1. Assasin       2. Barbarian       3. Knight
    hp = 5           hp = 8             hp = 10 
    str = 10         str = 7            str = 5 
    """))

    if namn == 1:
        Spelar_stats = (Assasin)
        print(" Du är nu en Assasin med 5 hp och 10 str")
        return
    elif namn == 2:
        Spelar_stats = (Barb)
        print(" Du är nu en Barbarian med 8 hp och 7 str")
        return
    elif namn == 3:
        Spelar_stats =(Knight)
        print(" Du är nu en Knight med 10 hp och 5 str")
        return
    else: 
        print("svara 1, 2 eller 3 din sopa")  
        karaktärsval()
       


def main():
    print("""
    Välkommen till Daedalus labyrint

    Ditt mål är att ta dig genom labyrinten men se upp för Taurus.
    Han har en slimekapasitet på 100%.
    """)

    karaktärsval()

    
main()