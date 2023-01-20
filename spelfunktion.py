import random
from karaktär import *
from text_animering import *

# ---------------------------------------- FIGHT ----------------------------------------


def fight(spelar_stats, monster_stats):
    typingPrint(
        f"Du stöter på en {monster_stats.m_namn} med {monster_stats.m_hp} hp och {monster_stats.m_str} str")
    if spelar_stats.p_str >= monster_stats.m_hp:
        typingPrint("du besegrade monstret")
        typingPrint(f"Du har {spelar_stats.p_hp} hp kvar")
        return (spelar_stats.p_hp)

    elif spelar_stats.p_str < monster_stats.m_hp and monster_stats.m_str >= spelar_stats.p_hp:
        typingPrint("du dog")
    elif spelar_stats.p_str < monster_stats.m_hp and monster_stats.m_str < spelar_stats.p_hp:
        monster_stats.m_hp = monster_stats.m_hp - spelar_stats.p_str
        spelar_stats.p_hp = spelar_stats.p_hp - monster_stats.m_str
        return (fight(spelar_stats, monster_stats))

# ---------------------------------------- FIGHT ----------------------------------------

# ---------------------------------------- VAPEN ----------------------------------------


class Vapen():
    def __init__(self, v_hp, v_str, v_namn):
        self.v_namn = v_namn
        self.v_hp = v_hp
        self.v_str = v_str


Svärd = Vapen(health(0, 1), damage(1, 2), "ett Svärd")
Sköld = Vapen(health(2, 3), damage(0, 0), "en Sköld")
Yxa = Vapen(health(0, 0), damage(1, 4), "en Yxa")
Pilbåge = Vapen(health(0, 0), damage(2, 3), "en Pilbåge")
Spjut = Vapen(health(0, 0), damage(1, 4), "ett Spjut")


# ---------------------------------------- VAPEN ----------------------------------------

# ---------------------------------------- RUM TYP OCH KISTA ----------------------------------------

def kista(Spelar_stats, v_hp, v_str, v_namn):
    vapen = random.choice([Svärd, Sköld, Yxa, Pilbåge, Spjut])
    typingPrint(
        f"du har hittat {v_namn}.\n det har en hp på {v_hp} och en styrka på {v_str}")
    if len(Spelar_stats.vapen_lista) > 2:
        Spelar_stats.vapen_lista.append(vapen)
    else:
        typingPrint(
            "Du har redan 2 vapen och måste ta bort ett vapen för att lägga till det nya")
        for i in range(len(Spelar_stats.vapen_lista)):
            typingPrint(
                f"indikations nummer = {i} {Spelar_stats[i].v_hp} {Spelar_stats[i].v_str} {Spelar_stats[i].v_namn}")
        while True:
            svar = typingInput(
                "Om du vill byta det nya vapnet mot ett gammalt vapen skriv in det gamla vapnets indikationsnummer annars skriv L ")
            if svar == "1":
                Spelar_stats.vapen_lista[1].pop()
                Spelar_stats.vapen_lista.append(vapen)
                return Spelar_stats
            elif svar == "2":
                Spelar_stats.vapen_lista[2].pop()
                Spelar_stats.vapen_lista.append(vapen)
                return Spelar_stats
            elif svar == "L" or "l":
                return Spelar_stats
            else:
                typingPrint("svara med ett av de givna alternativen")


def rum_typ(spelar_stats):
    typ = random.randint(1, 10)
    if typ in [1, 2, 3, 4]:
        monster_stats = monstrgenerator()
        spelar_stats.p_hp = fight(spelar_stats, monster_stats)
        val_vanlig(spelar_stats)
    elif typ in [5, 6, 7]:
        val_vanlig(spelar_stats)
    elif typ in [8, 9]:
        val_kista(spelar_stats)
    elif typ == 10:
        spelar_stats.p_hp = fälla(spelar_stats)
        val_vanlig(spelar_stats)


def fälla(spelar_stats):
    spelar_stats.p_hp -= 1
    typingPrint(f"du klev i en fälla, du har nu {spelar_stats.p_hp} hp kvar")
    return spelar_stats.p_hp


# ---------------------------------------- RUM TYP OCH KISTA ----------------------------------------
# ---------------------------------------- VALFUNKTIONER ----------------------------------------


def val_vanlig(spelar_stats):
    val = typingInput(
        "vad vill du göra?\n S = stats\n V = vänster\n F = fram\n H = höger\n R = ryggsäck\n")
    if val in ["S", "stats", "s"]:
        typingPrint(
            f"Du har hp {spelar_stats.p_hp} och din str är {spelar_stats.p_str}\n")
        val_vanlig(spelar_stats)
    elif val in ["V", "vänster", "v"]:
        typingPrint("du gick igen om dörren till vänster ")
        rum_typ(spelar_stats)
    elif val in ["H", "höger", "h"]:
        typingPrint("du gick igen om dörren till höger och kommer till ")
        rum_typ(spelar_stats)
    elif val in ["R", "ryggsäck", "r"]:
        typingPrint("hej")
    elif val in ["F", "fram", "f"]:
        typingPrint("Du går fram och kommer till ")
        rum_typ(spelar_stats)
    else:
        typingPrint("din sopa välj ett av alternativen")
        val_vanlig(spelar_stats)


def val_kista(spelar_stats):
    val = typingInput(
        "och hittade en kista. Vad vill du göra?\n S = stats\n Ö = öppna\n V = vänster\n H = höger\n ")
    if val in ["S", "stats", "s"]:
        typingPrint("din stats är dina stats")
        val_kista(spelar_stats)
    elif val in ["V", "vänster", "v"]:
        typingPrint("du gick igen om dörren till vänster och kommer till ")
        rum_typ(spelar_stats)
    elif val in ["H", "höger", "h"]:
        typingPrint("du gick igen om dörren till höger och kommer till ")
        rum_typ(spelar_stats)
    elif val in ["Ö", "öppna", "ö"]:
        typingPrint(
            "du öppnar kistan och med ett gnistlande ljud så ser du hur en stor  i den...")
        val_vanlig(spelar_stats)
    else:
        typingPrint("din sopa välj ett av alternativen")
        val_kista(spelar_stats)

# ---------------------------------------- VALFUNKTIONER ----------------------------------------

# ---------------------------------------- SPELFUNKTIONER ----------------------------------------


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
        return karaktärsval()


def main():
    typingPrint("""
    Välkommen till Daedalus labyrint

    Ditt mål är att ta dig genom labyrinten men se upp för Taurus.
    Han har en slimekapasitet på 100%.
    """)

    spelar_stats = karaktärsval()
    val_vanlig(spelar_stats)


main()

# ---------------------------------------- SPELFUNKTIONER ----------------------------------------
