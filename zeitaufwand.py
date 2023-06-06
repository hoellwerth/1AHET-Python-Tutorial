def durchschnitt(summe, arbeitstage):
    return summe / arbeitstage

arbeitstage = 1
summe = 0
zeit = 0
maximum = 0

print("Zeitaufwandrechner")

while zeit >= 0:
    zeit = int(input(f"Tag {arbeitstage} - Arbeitszeit: "))
    if zeit > maximum:
        maximum = zeit
    if zeit >= 0:
        summe += zeit
        arbeitstage += 1

print("Gesamtsumme der Arbeitsstunden: ", summe)
print("Anzahl Tage: ", arbeitstage - 1)
print("Maximale Tagesarbeitszeit: ", maximum)
print("Durchschnittliche Arbeitszeit pro Tag: ", durchschnitt(summe, arbeitstage))