import os

os.system("clear")

meine_liste = []

meine_liste.append(10)
meine_liste.append(20)
meine_liste.append(30)
meine_liste.append(40)
meine_liste.append(50)  

print(meine_liste)

print(sum(meine_liste))

meine_liste.remove(30)

print(40 in meine_liste)

andere_liste = [5, 10, 15, 20]

meine_liste.extend(andere_liste)

meine_liste.sort()

print(meine_liste)

meine_liste.clear()

print(len(meine_liste) == 0)