import os

os.system("clear")

schwein = []

schwein.append(100)

def gesamtSumme():
    summe = 0
    for i in schwein:
        summe += i

    return summe

def betragÄndern(delta):
    if (delta < 0 and abs(delta) > gesamtSumme()):
        return False
    
    schwein.append(delta)

    return True

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

for i in schwein:
    print(i)
print(gesamtSumme())