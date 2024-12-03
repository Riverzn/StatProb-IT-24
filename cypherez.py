from itertools import cycle

def vigenere_decrypt(ciphertext, key):
    key = cycle(key)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = 97 if char.islower() else 65
            shift = ord(next(key)) - 97
            plaintext += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            plaintext += char
    return plaintext

ciphertext = "cykahzmmvlyjktro"
key = "forest"
print(vigenere_decrypt(ciphertext, key))
