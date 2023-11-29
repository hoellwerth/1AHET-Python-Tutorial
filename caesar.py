import os

os.system("clear")

def caesarEncrypt(text, delta):
    encryptedText = ""
    for character in text:
        if character.isalpha():
            upperOffset = ord('A') if character.isupper() else ord('a')
            encryptedText += chr((ord(character) - upperOffset + delta) % 26 + upperOffset)
        else:
            encryptedText += character
    return encryptedText

def caesarDecrypt(text, delta):
    decryptedText = ""
    for character in text:
        if character.isalpha():
            upperOffset = ord('A') if character.isupper() else ord('a')
            decryptedText += chr((ord(character) - upperOffset - delta) % 26 + upperOffset)
        else:
            decryptedText += character
    return decryptedText

# Unit Test
text = "This is a unit test!"
if caesarDecrypt(caesarEncrypt(text, 3), 3) != text:
    print("\033[1m\033[93mTest Failed!\033[0m")
    exit()
    
print("\033[1m\033[92mTest Passed!\033[0m")

print(caesarDecrypt(caesarEncrypt("XYZ", 3), 3))