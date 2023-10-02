import math
import os 

os.system("clear")

start = float(input("Geben Sie den Startwert ein: "))
end = float(input("Geben Sie den Endwert ein: "))
step = float(input("Geben Sie die Schrittweite ein: "))

print("|______________________________________________________________|")
print("|      x-Wert        |         x^2        |         1/x        |")
print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
while start <= end:
    if abs(start - 0) < 0.0000000001:
        print("|           0        |        0           |  NICHT DEFINIERT   |")
    else:
        print("|      {0:8.4}      |      {1:8.4f}      |      {2:8.4f}      |".format(start, math.pow(start, 2), 1 / start))
    start += step