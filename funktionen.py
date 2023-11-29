import math

def zahlen_ausgeben(anfang, ende):
    zahl = anfang
    while zahl <= ende:
        if math.isqrt(zahl) ** 2 == zahl:
            print(zahl)
        zahl += 1

zahlen_ausgeben(1,5)

def createRectangle(length, width, symbol):
    for i in range(length):
        print(symbol, end="")
        for j in range(width):
            if i == 0 or i == length - 1:
                print(symbol, end="")
            else:
                print(" ", end="")            
        print(symbol)

createRectangle(10,10,"*")