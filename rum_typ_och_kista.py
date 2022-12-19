from spelfunktion import *
from vapen import *
from karaktär import *


def kista(Spelar_stats, v_hp, v_str, v_namn):
    inehåll = random.randint(1, 5)
    if inehåll == 1:
        typingPrint(
            f"du har hittat ett svärd.\n Svärdet har en hp på {v_hp} och en styrka på {v_str}")
        if len(Spelar_stats.vapen_lista) > 2:
            Spelar_stats.vapen_lista.append(Svärd)
        else:
            typingPrint(
                "Du har redan 2 vapen och måste ta bort ett vapen för att lägga till svärdet")
            for i in range(len(Spelar_stats.vapen_lista)):
                typingPrint(
                    f"indikations nummer = {i} {Spelar_stats[i].v_hp} {Spelar_stats[i].v_str} {Spelar_stats[i].v_namn}")
            while True:
                svar = typingInput(
                    "Om du vill byta svärdet mot ett vapen skriv in vapnets indikationsnummer annars skriv L ")
                if svar == "1":
                    Spelar_stats.vapen_lista[1].pop()
                    Spelar_stats.vapen_lista.append(Svärd)
                    return
                elif svar == "2":
                    Spelar_stats.vapen_lista[2].pop()
                    Spelar_stats.vapen_lista.append(Svärd)
                    return
                elif svar == "L" or "l":
                    return
                else:
                    typingPrint("svara med ett av de givna alternativen")

    elif inehåll == 2:
        typingPrint(
            f"du har hittat ett sköld.\n Sköld har en hp på {v_hp} och en styrka på {v_str}")
        if len(Spelar_stats.vapen_lista) > 2:
            Spelar_stats.vapen_lista.append(Sköld)
        else:
            typingPrint(
                "Du har redan 2 vapen och måste ta bort ett vapen för att lägga till skölden")
            for i in range(len(Spelar_stats.vapen_lista)):
                typingPrint(
                    f"indikations nummer = {i} {Spelar_stats[i].v_hp} {Spelar_stats[i].v_str} {Spelar_stats[i].v_namn}")
            while True:
                svar = typingInput(
                    "Om du vill byta skölden mot ett vapen skriv in vapnets indikationsnummer annars skriv L ")
                if svar == "1":
                    Spelar_stats.vapen_lista[1].pop()
                    Spelar_stats.vapen_lista.append(Sköld)
                    return
                elif svar == "2":
                    Spelar_stats.vapen_lista[2].pop()
                    Spelar_stats.vapen_lista.append(Sköld)
                    return
                elif svar == "L" or "l":
                    return
                else:
                    typingPrint("svara med ett av de givna alternativen")
    elif inehåll == 3:
        typingPrint(
            f"du har hittat ett yxa.\n Yxan har en hp på {v_hp} och en styrka på {v_str}")
        if len(Spelar_stats.vapen_lista) > 2:
            Spelar_stats.vapen_lista.append(Yxa)
        else:
            typingPrint(
                "Du har redan 2 vapen och måste ta bort ett vapen för att lägga till yxan")
            for i in range(len(Spelar_stats.vapen_lista)):
                typingPrint(
                    f"indikations nummer = {i} {Spelar_stats[i].v_hp} {Spelar_stats[i].v_str} {Spelar_stats[i].v_namn}")
            while True:
                svar = typingInput(
                    "Om du vill byta yxan mot ett vapen skriv in vapnets indikationsnummer annars skriv L ")
                if svar == "1":
                    Spelar_stats.vapen_lista[1].pop()
                    Spelar_stats.vapen_lista.append(Yxa)
                    return
                elif svar == "2":
                    Spelar_stats.vapen_lista[2].pop()
                    Spelar_stats.vapen_lista.append(Yxa)
                    return
                elif svar == "L" or "l":
                    return
                else:
                    typingPrint("svara med ett av de givna alternativen")

    elif inehåll == 4:
        typingPrint(
            f"du har hittat en pilbåge.\n Pilbågen har en hp på {v_hp} och en styrka på {v_str}")
        if len(Spelar_stats.vapen_lista) > 2:
            Spelar_stats.vapen_lista.append(Pilbåge)
        else:
            typingPrint(
                "Du har redan 2 vapen och måste ta bort ett vapen för att lägga till pilbågen")
            for i in range(len(Spelar_stats.vapen_lista)):
                typingPrint(
                    f"indikations nummer = {i} {Spelar_stats[i].v_hp} {Spelar_stats[i].v_str} {Spelar_stats[i].v_namn}")
            while True:
                svar = typingInput(
                    "Om du vill byta pilbågen mot ett vapen skriv in vapnets indikationsnummer annars skriv L ")
                if svar == "1":
                    Spelar_stats.vapen_lista[1].pop()
                    Spelar_stats.vapen_lista.append(Pilbåge)
                    return
                elif svar == "2":
                    Spelar_stats.vapen_lista[2].pop()
                    Spelar_stats.vapen_lista.append(Pilbåge)
                    return
                elif svar == "L" or "l":
                    return
                else:
                    typingPrint("svara med ett av de givna alternativen")

    elif inehåll == 5:
        typingPrint(
            f"du har hittat ett spjut.\n Spjut har en hp på {v_hp} och en styrka på {v_str}")
        if len(Spelar_stats.vapen_lista) > 2:
            Spelar_stats.vapen_lista.append(Spjut)
        else:
            typingPrint(
                "Du har redan 2 vapen och måste ta bort ett vapen för att lägga till sjutet")
            for i in range(len(Spelar_stats.vapen_lista)):
                typingPrint(
                    f"indikations nummer = {i} {Spelar_stats[i].v_hp} {Spelar_stats[i].v_str} {Spelar_stats[i].v_namn}")
            while True:
                svar = typingInput(
                    "Om du vill byta spjutet mot ett vapen skriv in vapnets indikationsnummer annars skriv L ")
                if svar == "1":
                    Spelar_stats.vapen_lista[1].pop()
                    Spelar_stats.vapen_lista.append(Spjut)
                    return
                elif svar == "2":
                    Spelar_stats.vapen_lista[2].pop()
                    Spelar_stats.vapen_lista.append(Spjut)
                    return
                elif svar == "L" or "l":
                    return
                else:
                    typingPrint("svara med ett av de givna alternativen")


kista()


def rum_typ(spelar_stats):
    typ = random.randint(1, 10)
    if typ == 1 or typ == 2 or typ == 3 or typ == 4:
        monster_stats=monstrgenerator()
        spelar_stats.p_hp=fight(spelar_stats,monster_stats)
        val_vanlig(spelar_stats)
    elif typ == 5 or typ == 6 or typ == 7 or typ == 8:
        val_vanlig(spelar_stats)
    elif typ == 9:
        val_kista()
    elif typ == 10:
        fälla(spelar_stats)
        val_vanlig(spelar_stats)


def fälla(p_hp):
    p_hp -= 1
    typingPrint(f"du klev i en fälla, du har nu {p_hp} hp kvar")
    return p_hp
