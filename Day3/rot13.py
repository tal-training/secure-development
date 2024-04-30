import string

def encrypt_rot13(cleartext):
    cipher=""
    for c in cleartext:
        index=string.ascii_lowercase.index(c)
        char=string.ascii_lowercase[(index+13)%26]
        cipher+=char
    return cipher

def decrypt_rot13(ciphertext):
    clear=""
    for c in ciphertext:
        index=string.ascii_lowercase.index(c)
        char=string.ascii_lowercase[(index-13)%26]
        clear+=char
    return clear


print(encrypt_rot13("hello  world"))
print(decrypt_rot13(encrypt_rot13("helloworld")))
