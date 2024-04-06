from flask import Flask, send_file, session, render_template, request, redirect
from faker import Faker
import sqlite3
import json

app = Flask(__name__)

app.secret_key="12345678"

def query(sql, v=()):
    with sqlite3.connect("./data.db") as conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, doctor TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, data_id INTEGER, FOREIGN KEY(data_id) REFERENCES data(id))")
        cur.execute(sql, v)
        try:
            return {
                "data":[dict(zip([t[0] for t in cur.description], r)) for r in cur.fetchall()],
                "id":cur.lastrowid
            }
        except Exception as e:
            return e

def create_fake_data(num=100):
    for i in range(num):
        username=Faker().name()
        user_id=query(f"INSERT INTO data (name, date, doctor) VALUES ('{username}', '{Faker().date()}', '{Faker().name()}')")["id"]
        query(f"INSERT INTO users (username, password, data_id) VALUES ('{username.lower().split(' ')[0]}', '1234', '{user_id}')")


@app.route('/')
def home():
    if session.get("user", False):
        return send_file("static/index.html")
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    if query("select * from users where username=? and password=?", (request.form["username"],request.form["password"]))!=[]:
        session["user"]={"username":request.form["username"]}
        return redirect("/")
    else:
        return "login failed"


@app.route('/api/data')
def get_all_data():
    return json.dumps(query("SELECT * FROM data"))

if __name__=="__main__":
    create_fake_data()