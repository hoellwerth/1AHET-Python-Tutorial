def rabatt(gesamtpreis):
    if gesamtpreis >= 1000:
        return 0.9
    
    if gesamtpreis >= 500:
        return 0.95
    
    return 0

def einlesen():
    stückzahl = int(input("Stückzahl: "))

    if stückzahl == 0:
        return
    
    preis = float(input("Preis: "))

    return stückzahl * preis

if __name__ == "__main__":
    sum = 0
    while True:
        eingelesen = einlesen()
        if (not eingelesen):
            break
        
        sum += eingelesen
        
    print(f"Preis vor Rabatt: {sum}€")
    print(f"Rabatt: {rabatt(sum)}%")
    print(f"Gesamtpreis: {rabatt(sum) * sum}€")