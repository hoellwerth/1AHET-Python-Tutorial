def Zahlenreihe(factor, end):
    for i in range(1, end + 1):
        print(f"{i} x {factor} = {i * factor}")

def einmaleins():
    for i in range(1, 11):
        Zahlenreihe(i, 10)

factor = int(input("Gib die Multiplikationsreihe ein: "))
end = int(input("Gib die gewünschte letzte Zahl ein: "))

Zahlenreihe(factor, end)
einmaleins()

