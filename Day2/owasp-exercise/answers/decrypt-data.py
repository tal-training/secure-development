from cryptography.fernet import Fernet

key = input("enter the key: ").encode()

try:
    cipher_suite = Fernet(key)
except:
    print("wrong key")
    exit()

decrypted_data = cipher_suite.decrypt(open("data.crypt","rb").read())

print(decrypted_data)