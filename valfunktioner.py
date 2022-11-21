
def val():
    val = input(
        "vad vill du göra?\n K = kamp\n S = stats\n Ö = öppna\n V = vänster\n H = höger\n ")
    if val == "S" or val == "stats" or val == "s":
        print("din stats är dina stats")
    elif val == "V" or val == "vänster" or val == "v":
        print("du gick igen om dörren till vänster och kommer till...")
    elif val == "H" or val == "höger" or val == "h":
        print("du gick igen om dörren till höger och kommer till...")
    elif val == "Ö" or val == "öppna" or val == "ö":
        print("du öppnar kistan och med ett gnistlande ljud så ser du hur en stor  i den...")
    elif val == "K" or val == "kamp" or val == "k":
        print("du knyter dina nävar och gör dig redo...")
    else:
        print("din sopa välj ett av alternativen")
ja