import os 

os.system("clear")

kasse = list()

def rabatt(gesamtpreis):
    if gesamtpreis >= 1000:
        return 0.9

    if gesamtpreis >= 500:
        return 0.95

    return 1

def einlesen():
    try:
        stückzahl = int(input("Stückzahl: "))
    except:
        print("Bitte gib eine Zahl ein!")
        return None

    if stückzahl == 0:
        return False
    try:
        preis = float(input("Preis: "))
    except:
        print("Bitte gib eine Zahl ein!")
        return None

    try:
        produktname = input("Produktname: ")
    except:
        print("Bitte gib eine Zahl ein!")
        return None

    return [stückzahl, preis, produktname]

if __name__ == "__main__":
    while True:
        eingelesen = einlesen()

        if (eingelesen == None):
            continue
        if (not eingelesen):
            break

        kasse.append(eingelesen)

    summe = 0

    print("                       Rechnung                       ")
    print("──────────────────────────────────────────────────────")
    print("     Name    | Stückzahl  | Stückpreis |    Preis     ")
    print("──────────────────────────────────────────────────────")

    for i in kasse:
        preis = i[0] * i[1]
        summe += preis

        print("  {:10s} | {:10d} | {:10.2f} | {:11.2f} ".format(i[2], i[0], i[1], preis))

    print("──────────────────────────────────────────────────────")
    print("     Preis vor Rabatt     |   Rabatt   |   Endpreis   ")
    print("──────────────────────────────────────────────────────")
    print("  {:23.2f} | {:9.2f}% | {:11.2f}€ ".format(summe, rabatt(summe), rabatt(summe) * summe))