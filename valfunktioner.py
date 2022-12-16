from text_animering import *
from fight import *
from Karaktärer import *


def val_vanlig(p_hp, p_str):
    val = typingInput(
        "vad vill du göra?\n S = stats\n V = vänster\n H = höger\n R = ryggsäck\n")
    if val == "S" or val == "stats" or val == "s":
        typingPrint(f"din hp är nu {p_hp} och din str är {p_str}")
        val_vanlig(p_hp, p_str)
    elif val == "V" or val == "vänster" or val == "v":
        typingPrint("du gick igen om dörren till vänster och kommer till...")
    elif val == "H" or val == "höger" or val == "h":
        typingPrint("du gick igen om dörren till höger och kommer till...")
    elif val == "Ö" or val == "öppna" or val == "ö":
        typingPrint(
            "du öppnar kistan och med ett gnistlande ljud så ser du hur en stor  i den...")
    elif val == "R" or val == "ryggsäck" or val == "r":
        typingPrint("hej")
    else:
        typingPrint("din sopa välj ett av alternativen")
        val_vanlig()


def val_kista():
    val = typingInput(
        "vad vill du göra?\n S = stats\n Ö = öppna\n V = vänster\n H = höger\n ")
    if val == "S" or val == "stats" or val == "s":
        typingPrint("din stats är dina stats")
        val_kista()
    elif val == "V" or val == "vänster" or val == "v":
        typingPrint("du gick igen om dörren till vänster och kommer till...")
    elif val == "H" or val == "höger" or val == "h":
        typingPrint("du gick igen om dörren till höger och kommer till...")
    elif val == "Ö" or val == "öppna" or val == "ö":
        typingPrint(
            "du öppnar kistan och med ett gnistlande ljud så ser du hur en stor  i den...")
        val_vanlig()
    else:
        typingPrint("din sopa välj ett av alternativen")
        val_kista()
