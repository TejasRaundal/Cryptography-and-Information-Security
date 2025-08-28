# Caesar Cipher (Monoalphabetic)
def caesar_encrypt(plainText,key):
    cipherText = ""

    for ch in plainText:
        if ch.isupper():
            ch = chr((ord(ch)-ord('A') + key) % 26 + ord('A'))
        elif ch.islower():
            ch = chr((ord(ch)-ord('a') + key) % 26 + ord('a'))
        cipherText += ch

    return cipherText
    

def caesar_decrypt(plainText,key):
    cipherText = ""

    for ch in plainText:
        if ch.isupper():
            ch = chr((ord(ch)-ord('A') - key) % 26 + ord('A'))
        elif ch.islower():
            ch = chr((ord(ch)-ord('a') - key) % 26 + ord('a'))
        cipherText += ch

    return cipherText


plainText = input("Enter the Message: ")
key = int(input("Enter the integer key: "))

encrypted=caesar_encrypt(plainText,key)
print(f"Encrypted of {plainText} : {encrypted}")

decrypted = caesar_decrypt(encrypted,key)
print(f"Decrypted of {encrypted} : {decrypted}")