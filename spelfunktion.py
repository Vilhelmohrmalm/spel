import random
from karaktär import *
from text_animering import *


# ---------------------------------------- SLUT  ----------------------------------------

def slut():
    typingPrint("Game Over")
    quit()

# ---------------------------------------- SLUT  ----------------------------------------

# ---------------------------------------- FIGHT ----------------------------------------


def fight(spelar_stats, monster_stats):
    typingPrint(
        f"och du stöter på en {monster_stats.m_namn} med {monster_stats.m_hp} hp och {monster_stats.m_str} str\n")
    while monster_stats.m_hp > 0:
        if spelar_stats.p_str + spelar_stats.vapen.v_str >= monster_stats.m_hp:
            typingPrint("du besegrade monstret\n")
            typingPrint(f"Du har {spelar_stats.p_hp} hp kvar\n")
            spelar_stats.p_lvl += 1
            typingPrint(f"Du är är nu lvl {spelar_stats.p_lvl}\n")
            return (spelar_stats)

        elif spelar_stats.p_str + spelar_stats.vapen.v_str < monster_stats.m_hp and monster_stats.m_str >= spelar_stats.p_hp + spelar_stats.vapen.v_hp:
            typingPrint("du dog\n")
            slut()
        elif spelar_stats.p_str + spelar_stats.vapen.v_str < monster_stats.m_hp and monster_stats.m_str < spelar_stats.p_hp + spelar_stats.vapen.v_hp:
            monster_stats.m_hp = monster_stats.m_hp - \
                spelar_stats.p_str - spelar_stats.vapen.v_str
            spelar_stats.p_hp = spelar_stats.p_hp - \
                monster_stats.m_str + spelar_stats.vapen.v_hp


# ---------------------------------------- FIGHT ----------------------------------------

# ---------------------------------------- RUM TYP OCH KISTA ----------------------------------------

def kista(spelar_stats):

    Svärd = Vapen(health(0, 1), damage(1, 2), "ett Svärd")
    Sköld = Vapen(health(1, 2), damage(0, 0), "en Sköld")
    Yxa = Vapen(health(0, 0), damage(1, 4), "en Yxa")
    Pilbåge = Vapen(health(0, 0), damage(1, 3), "en Pilbåge")
    Spjut = Vapen(health(0, 0), damage(2, 3), "ett Spjut")

    vapen = random.choice([Svärd, Sköld, Yxa, Pilbåge, Spjut])
    typingPrint(
        f"{vapen.v_namn}.\n det har en hp på {vapen.v_hp} och en styrka på {vapen.v_str}\n")

    typingPrint(
        "Du måste ta bort ditt nuvarande vapen för att ta det nya\n")

    typingPrint(
        f"Du har {spelar_stats.vapen.v_namn} med {spelar_stats.vapen.v_hp} hp och {spelar_stats.vapen.v_str} str\n ")
    while True:
        svar = typingInput(
            "Om du vill byta det nya vapnet mot det gammla vapnet skriv in 1 annars skriv L \n")
        if svar == "1":
            typingPrint("du har nu ett nytt vapen i din ryggsäck\n")
            spelar_stats.vapen = vapen
            return spelar_stats
        elif svar == "L" or "l":
            typingPrint(
                "du lämnade det nya fräsha vapnet i kistan för du kan inte överge ditt gamla vapen efter allt ni gjort tilsammans\n")
            return spelar_stats
        else:
            typingPrint("svara med ett av de givna alternativen")


def rum_typ(spelar_stats):
    typ = random.randint(1, 10)
    if typ in [1, 2, 3, 4]:
        monster_stats = monstrgenerator()
        spelar_stats = fight(spelar_stats, monster_stats)
        return (spelar_stats)
    elif typ in [5, 6]:
        typingPrint("och kommer till ett tomt rum\n")
        return (spelar_stats)
    elif typ in [7, 8]:
        val_kista(spelar_stats)
        return (spelar_stats)
    elif typ in [9, 10]:
        fälla(spelar_stats)
        return (spelar_stats)


def fälla(spelar_stats):
    if spelar_stats.p_hp > 1:
        spelar_stats.p_hp -= 1
        typingPrint(
            f"där du klev i en fälla, du har nu {spelar_stats.p_hp} hp kvar\n")
        return spelar_stats
    else:
        typingPrint("där du dör i en fälla\n")
        slut()


# ---------------------------------------- RUM TYP OCH KISTA ----------------------------------------
# ---------------------------------------- VALFUNKTIONER ----------------------------------------


def val_vanlig(spelar_stats):
    while spelar_stats.p_lvl <= 9:
        val = typingInput(
            "vad vill du göra?\n S = stats\n V = vänster\n F = fram\n H = höger\n R = ryggsäck\n")
        if val in ["S", "stats", "s"]:
            typingPrint(
                f"Du har {spelar_stats.p_hp} hp, din str är {spelar_stats.p_str} och din lvl är {spelar_stats.p_lvl}\n")

        elif val in ["V", "vänster", "v"]:
            typingPrint("du går igenom dörren till vänster ")
            rum_typ(spelar_stats)
        elif val in ["H", "höger", "h"]:
            typingPrint("du går igenom dörren till höger ")
            rum_typ(spelar_stats)
        elif val in ["R", "ryggsäck", "r"]:
            typingPrint(
                f"Du har {spelar_stats.vapen.v_namn} med {spelar_stats.vapen.v_hp} hp {spelar_stats.vapen.v_str} str \n")
        elif val in ["F", "fram", "f"]:
            typingPrint("Du går igenom dörren framför dig ")
            rum_typ(spelar_stats)
        else:
            typingPrint("din sopa välj ett av alternativen\n")

    return ()


def val_kista(spelar_stats):
    val = typingInput(
        "och hittar en kista. Vad vill du göra?\n S = stats\n Ö = öppna\n L = lämna kistan\n")
    if val in ["S", "stats", "s"]:
        typingPrint(
            f"Du har hp {spelar_stats.p_hp}, din str är {spelar_stats.p_str} och din lvl är {spelar_stats.p_lvl}\n")
        return val_kista(spelar_stats)
    elif val in ["Ö", "öppna", "ö"]:
        typingPrint(
            "du öppnar kistan och i den hittar du ")
        kista(spelar_stats)
        return spelar_stats
    elif val in ["L", "lämna kistan", "lämna", "l"]:
        typingPrint("du lämnar kistan där för att rutna, utan att någonsinn få veta vad som finns i den.\nKistans inehåll kommer att förbli ett mysterium för alltid.\n")
        return spelar_stats
    else:
        typingPrint("din sopa välj ett av alternativen")
        return val_kista(spelar_stats)

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
        typingPrint(" Du är nu en Assasin med 5 hp och 10 str \n")
        return (Spelar_stats)

    elif namn == 2:
        Spelar_stats = (Barb)
        typingPrint(" Du är nu en Barbarian med 8 hp och 7 str \n")
        return (Spelar_stats)

    elif namn == 3:
        Spelar_stats = (Knight)
        typingPrint(" Du är nu en Knight med 10 hp och 5 str \n")
        return (Spelar_stats)

    else:
        typingPrint("svara 1, 2 eller 3 din sopa\n")
        return karaktärsval()


def main():
    typingPrint("""
    Välkommen till Daedalus labyrint

    Ditt mål är att nå lvl 10 men se upp för Taurus.
    Han har en slimekapasitet på 100%.
    """)

    spelar_stats = karaktärsval()

    val_vanlig(spelar_stats)

    typingPrint("Grattis du vann\n")
    slut()


main()

# ---------------------------------------- SPELFUNKTIONER ----------------------------------------
