import os

os.system("clear")

einheiten = (1, 2, 5, 10, 20, 50, 100, 200, 500)

schwein = []

def gesamtSumme():
    summe = 0
    for i in schwein:
        summe += i[0][0] * i[0][1]

    return summe

def betragÄndern(delta):
    if (delta < 0 and abs(delta) > gesamtSumme()):
        return False
    
    schwein.append(teileGeld(delta))

    return True

def teileGeld(geld):
    geteiltesGeld = list()

    for i in range(len(einheiten), 0, -1):
        div = divmod(geld, einheiten[i - 1])
        if div[1] == geld: # Zu klein
            continue

        geteiltesGeld.append([div[0], einheiten[i - 1]])
        geld = div[1]

    return geteiltesGeld # [  [[ anzahl, schein ], [ anzahl, schein ]], [ anzahl, schein ]]...]

schwein.append(teileGeld(100))

def berechneScheine():
    scheine = [0] * len(einheiten)

    for i in schwein:
        for j in i:
            scheine[einheiten.index(j[1])] = scheine[einheiten.index(j[1])] + j[0]

    return scheine

while True:
    try:
        betrag = int(input("Gib den den Betrag ein: (\"0\" zum beenden) "))
    except:
        os.system("clear")
        print("Bitte gib eine Zahl ein! (\"0\" zum beenden)")
        
        continue

    os.system("clear")

    if (betrag == 0):
        break;

    if (not betragÄndern(betrag)):
        print(f"Du hast nicht genug Geld. Dir fehlen {abs(gesamtSumme() + betrag)} um {betrag} zu beheben!")

scheine = berechneScheine()

print(scheine)

count = 0
for i in range(len(scheine)):
    if (scheine[i] == 0):
        continue

    count += 1

    print(f"{count}. {scheine[i]} * {einheiten[i]}")

print(f"Endsumme: {gesamtSumme()}")