# 1.
mein_tupel = ("Apfel", "Banane", "Kirsche", "Dattel", "Erdbeere")

# 2.
print(mein_tupel)

# 3.
try:
    mein_tupel[0] = "Birne"
except TypeError:
    print("Tupel sind unveränderlich")

# 4.
anderes_tupel = (1, 2, 3)

# 5.
kombiniertes_tupel = mein_tupel + anderes_tupel

# 6.
print(kombiniertes_tupel)

# 7.
print(len(kombiniertes_tupel))

# 8.
print("Banane" in kombiniertes_tupel)

# 9.
zahlen_tupel = (5, 10, 15, 20)

# 10.
verdoppeltes_tupel = tuple([x * 2 for x in zahlen_tupel])

# 11.
print(verdoppeltes_tupel)

# 12.
gemischtes_tupel = ("Apfel", 5, "Banane", 10)

# 13.
print(gemischtes_tupel)

# 14.
print(len([x for x in gemischtes_tupel if type(x) == str]))

print(len([x for x in gemischtes_tupel if type(x) == int]))

# 15.
kombiniertes_tupel = tuple([str(x) for x in kombiniertes_tupel])
sortiertes_tupel = tuple(sorted(kombiniertes_tupel))

# 16.
print(sortiertes_tupel)
