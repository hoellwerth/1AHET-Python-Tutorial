import os
import datetime as datetime

os.system("clear")

temperaturen = list()
luftdruecke = list()

datetime.datetime.today()
def eingabe():
    while True:
        try:
            temperatur = int(input("Geben Sie die aktuelle Temperatur ein: (0 zum beenden) "))
        except:
            print("Bitte geben Sie eine Zahl ein!")
            continue

        if temperatur == 0:
            break
        
        try:
            luftdruck = int(input("Geben Sie die aktuelle Luftdruck ein: (0 zum beenden) "))
        except:
            print("Bitte geben Sie eine Zahl ein!")
            continue

        if luftdruck == 0:
            break
        
        temperaturen.append([datetime.datetime.today(), temperatur])
        luftdruecke.append([datetime.datetime.today(), luftdruck])

def ausgeben(werte):
    minimum = werte[0][1]
    maximum = werte[0][1]
    summe = 0

    for i in range(len(werte)):
        if werte[i][1] < minimum:
            minimum = werte[i][1]

        if werte[i][1] > maximum:
            maximum = werte[i][1]

        summe += werte[i][1]

    print(f"Minimum: {minimum}")
    print(f"Maximal: {maximum}")
    print(f"Durchschnitt: {summe / len(werte)}")

eingabe()

print("------------------Temperaturen(°C)--------------")
ausgeben(temperaturen)

print("-------------------Luftdruck(hPa)---------------")
ausgeben(luftdruecke)