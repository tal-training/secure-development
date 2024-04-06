from cryptography.fernet import Fernet
import base64

key = Fernet.generate_key()

print("YOU HAVE TO STORE THIS KEY TO DECRYPT YOUR DATA: ",key)

cipher_suite = Fernet(key)

data = input("Enter data to encrypt: ").encode()

encrypted_data = cipher_suite.encrypt(data)

open("data.crypt","wb").write(encrypted_data)

