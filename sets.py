# 1.
mein_set = set()

# 2.
mein_set = {"Apfel", "Banane", "Kirsche", "Dattel", "Erdbeere"}

# 3.
print(mein_set)

# 4.
try:
    mein_set.add("Apfel")
except TypeError:
    print("Sets sind unveränderlich")

# 5.
anderes_set = {"Banane", "Orange", "Kiwi"}

# 6.
print(anderes_set)

# 7.
schnittmenge = mein_set.intersection(anderes_set)

# 8.
print(schnittmenge)

# 9.
vereinigtes_set = mein_set.union(anderes_set)

# 10.
print(vereinigtes_set)

# 11.
mein_set.remove("Kirsche")

# 12.
print(mein_set.isdisjoint(anderes_set))

# 13.
zahlen_set = {1, 2, 3, 4, 5}

# 14.
print(all([x % 2 == 0 for x in zahlen_set]))

# 15.
leeres_set = set()
print(len(leeres_set) == 0)

# 16.
mein_set.clear()

# 17.
print(len(mein_set) == 0)