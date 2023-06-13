from random import randint

def pasch(versuche):
    pasche = 0
    for _ in range(versuche):
        w1 = randint(1,6)
        w2 = randint(1,6)
        if w1 == w2:
            pasche += 1
            print(f"{w1} {w2} - Pasch")
            continue

        print(w1, w2)
    
    return pasche

def überprüfeSchätzung(pasche, schätzung):
    if pasche == schätzung:
        print(f"Die Schätzung ({schätzung}) war richtig!")
        return
    
    if pasche > schätzung:
        print(f"Die Schätzung ({schätzung}) war zu niedrig! - Es wurden {pasche} Pasche gewürfelt.")
        return
    
    print(f"Die Schätzung ({schätzung}) war zu hoch! - Es wurden {pasche} Pasche gewürfelt.")


würfelAnzahl = int(input("Wie oft soll gewürfelt werden: "))
schätzung = int(input("Wie viele pasche werden gewürfelt: "))

überprüfeSchätzung(pasch(würfelAnzahl), schätzung)
