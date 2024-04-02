admin_password="hashed_admin_password"

permissions={
    "user1":"user",
    "admin":"admin"
}

passwords={
    "user1":"hashed_password",
}

def make_admin(username):
    if admin_login():
        permissions[username]=="admin"

def recover_password(username):
    if admin_login():
        passwords[username]=input(f"enter new password for {username}: ") 

def get_sensitive_data(username):
    if is_admin(username):
        return "sensitive data"

def is_admin(username):
    return check_permission(username)=="admin"

def check_permission(username):
    return permissions[username]

def login(username="user1"):
    return (input("username: "), input("password: "))==(username, passwords[username])

def admin_login():
    return (input("password: "))==(admin_password)

if __name__=="__main__":
    login()
    # add application logic here...

