import os

os.system("clear")

kaffeeliste = { 'Peter': 0, 'Paul': 0, 'Maria': 0 }
teeliste = { 'Peter': 0, 'Paul': 0, 'Maria': 0 }

def createEmployee(name):
    if name not in kaffeeliste:
        kaffeeliste[name] = 0
        teeliste[name] = 0

        return True
    return False

while True:
    name = input("Wer säuft dieses Gesöff? (Enter zum Abrechnen): ")
    
    if name == "":
        break

    if (name in kaffeeliste) or (name in teeliste):
        getränk = input(f"Welches Gesöff wird von {name} gesoffen (Kaffee oder Tee) (Enter zum Abrechnen): ")

        if getränk == "":
            break

        if getränk == "Kaffee":
            kaffeeliste[name] += 1

            print(kaffeeliste[name])

            continue

        if getränk == "Tee":
            teeliste[name] += 1

            print(teeliste[name])

            continue

        print("Falsches Getränk! Bitte nur \"Kaffee\" oder \"Tee\" eingeben.")

        continue

    if ("Ja" == input("Der Mitarbeiter existiert nicht. Möchtest du ihn erstellen? (Ja / Nein): ")):

        createEmployee(name)

        print(f"Der Mitarbeiter {name} wurde in die Listen eingetragen.")

print("Kaffeeliste:", kaffeeliste)
print("Teeliste:", teeliste)