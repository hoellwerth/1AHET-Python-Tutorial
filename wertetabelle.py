import math
import os 

os.system("clear")

start = float(input("Geben Sie den Startwert ein: "))
end = float(input("Geben Sie den Endwert ein: "))
step = float(input("Geben Sie die Schrittweite ein: "))

def decimal_range(start, stop, increment):
    while start < stop and not math.isclose(start, stop):
        yield start
        start += increment


def getOneThroughX(start, end, step):
    oneThroughX = []

    for i in decimal_range(start, end, step):
        if (i == 0):
            oneThroughX.append("NICHT DEFINIERT")
            continue

        oneThroughX.append(1 / i)

    return oneThroughX

def getXToThePowerOf2(start, end, step):
    XToThePowerOf2 = []

    for i in decimal_range(start, end, step):
        XToThePowerOf2.append(math.pow(i, 2))

    return XToThePowerOf2

def getHeader():
    print("|______________________________________________________________|")
    print("|      x-Wert        |         x^2        |         1/x        |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")

def printLines():
    division = getOneThroughX(start, end, step)
    power = getXToThePowerOf2(start, end, step)

    for i in range(len(division)):
        if (division[i] == "NICHT DEFINIERT"):
            print("|      {0:8}      |      {1:8.4f}      |  NICHT DEFINIERT   |".format(i, power[i]))
            continue

        print("|      {0:8}      |      {1:8.4f}      |      {2:8.4f}      |".format(i, power[i], division[i]))


getHeader()

printLines()