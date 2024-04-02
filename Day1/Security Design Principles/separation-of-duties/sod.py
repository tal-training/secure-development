# Exercise: refactor the following script according to the separation of duties principle.

def login():
    if (input("username: "), input("password: "))==("user1", "1234"):
        if input("are you admin? ").startswith('y'):
            print("secret data...")
        else:
            if input("do you want to be admin? ").startswith('y'):
                print("You are now admin. Here is secret data...")
    else:
        if input("do you want to recover password for user1? ").startswith('y'):
            print("1234")

if __name__=="__main__":
    login()

