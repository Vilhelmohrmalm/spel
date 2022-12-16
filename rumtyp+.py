from spelfunktion import *
from vapen import *
from Karaktärer import *


def kista(Spelar_stats, v_hp, v_str, v_namn):
    inehåll = random.randint(1, 5)
    if inehåll == 1:
        typingPrint(
            f"du har hittat ett svärd.\n Svärdet har en hp på {v_hp} och en styrka på {v_str}")
        if len(Spelar_stats.vapen_lista) > 2:
            Spelar_stats.vapen_lista.append(Svärd)
        else:
            print(
                "Du har redan 2 vapen och måste ta bort ett vapen för att lägga till svärdet")
            for i in range(len(Spelar_stats.vapen_lista)):
                print(
                    f"indikations nummer = {i} {Spelar_stats[i].v_hp} {Spelar_stats[i].v_str} {Spelar_stats[i].v_namn}")
            while True:
                svar = typingInput(
                    "Om du vill byta bort svärdet mot ett vapen skriv in vapnets indikationsnummer annars skriv L ")
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
            print(
                "Du har redan 2 vapen och måste ta bort ett vapen för att lägga till skölden")
            for i in range(len(Spelar_stats.vapen_lista)):
                print(
                    f"indikations nummer = {i} {Spelar_stats[i].v_hp} {Spelar_stats[i].v_str} {Spelar_stats[i].v_namn}")
            while True:
                svar = typingInput(
                    "Om du vill byta bort skölden mot ett vapen skriv in vapnets indikationsnummer annars skriv L ")
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
            f"du har hittat ett yxa.\n Svärdet har en hp på {v_hp} och en styrka på {v_str}")
        if len(Spelar_stats.vapen_lista) > 2:
            Spelar_stats.vapen_lista.append(Yxa)
        else:
            print(
                "Du har redan 2 vapen och måste ta bort ett vapen för att lägga till svärdet")
            for i in range(len(Spelar_stats.vapen_lista)):
                print(
                    f"indikations nummer = {i} {Spelar_stats[i].v_hp} {Spelar_stats[i].v_str} {Spelar_stats[i].v_namn}")
            while True:
                svar = typingInput(
                    "Om du vill byta bort svärdet mot ett vapen skriv in vapnets indikationsnummer annars skriv L ")
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

    elif inehåll == 4:
        Spelar_stats.vapen_lista.append(Pilbåge)

    elif inehåll == 5:
        Spelar_stats.vapen_lista.append(Spjut)


kista()


def rum_typ(p_hp, p_str):
    typ = random.randint(1, 10)
    if typ == 1 or typ == 2 or typ == 3 or typ == 4:
        fight(p_hp, p_str)
        val_vanlig(p_hp, p_str)
    elif typ == 5 or typ == 6 or typ == 7 or typ == 8:
        val_vanlig(p_hp, p_str)
    elif typ == 9:
        val_kista()
    elif typ == 10:
        fälla()
        val_vanlig()


def fälla(p_hp):
    p_hp -= 1
    typingPrint(f"du klev i en fälla, du har nu {p_hp} hp kvar")
    return p_hp
