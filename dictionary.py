import os

os.system("clear")

# 1.
mein_dict = {}

# 2.
mein_dict["Name"] = "Max"
mein_dict["Alter"] = 30
mein_dict["Stadt"] = "Berlin"
mein_dict["Beruf" ] = "Ingenieur"

# 3.
print(mein_dict)

# 4.
print(mein_dict["Alter"])

# 5.
mein_dict["Stadt"] = "Hamburg"

# 6.
mein_dict["Hobby"] = "Schwimmen"

# 7.
print(mein_dict.keys())

#8.
print(mein_dict.values())

# 9.
print("Beruf" in mein_dict)

# 10.
mein_dict.pop("Hobby")

# 11,
anderes_dict = {
    "Land": "Frankreich",
    "Bevölkerung": 67_000_000
}

# 12.
mein_dict.update(anderes_dict)

# 13.
print(mein_dict)

# 14.
print(len(mein_dict))

# 15.
leeres_dict = {}
print(len(leeres_dict) == 0)

# 16.
mein_dict.clear()

# 17.
print(len(mein_dict) == 0)