###### Solution (Python Example)
import hashlib
import pickle

password=input("Hi user, please choose a password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

passwords = {"user":hashed_password}

with open("passwords.pkl", "wb") as f:
    pickle.dump(passwords, f)
    print("password saved")

def login():
    password=input("enter password for user: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open("passwords.pkl", "rb") as f:
        hash=pickle.load(f)["user"]
        print(hash, hashed_password)
        if hash==hashed_password:
            print("login successful")
        else:
            print("unauthorized")

login()