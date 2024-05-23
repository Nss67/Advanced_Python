
clear_text = input("write your messages: ")


def encrypt(plaintext, _key):
    enc = ""
    for i in range(len(plaintext)):
        c = chr(ord(plaintext[i]) + int(_key + _key))
        enc += c
    return enc


def decrypt(ciphertext, _key):
    enc = ""
    for i in range(len(ciphertext)):
        c = chr(ord(ciphertext[i]) - int(_key + _key))
        enc += c
    return enc


_key = 50

encrypted_text = encrypt(clear_text, _key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, _key)
print("Decrypted text:", decrypted_text)
