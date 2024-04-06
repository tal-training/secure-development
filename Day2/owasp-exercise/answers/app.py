from flask import Flask, send_file, make_response
from faker import Faker
import sqlite3
import json
import random
import base64

app = Flask(__name__)

def query(sql, v=()):
    with sqlite3.connect("./data.db") as conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, doctor TEXT)")
        cur.execute(sql, v)
        try:
            return [dict(zip([t[0] for t in cur.description], r)) for r in cur.fetchall()]
        except:
            return ""

def create_fake_data(num=100):
    for i in range(num):
        query(f"INSERT INTO data (name, date, doctor) VALUES ('{Faker().name()}', '{Faker().date()}', '{Faker().name()}')")

@app.route('/')
def home():
    return send_file("static/index.html")

@app.route('/token')
def get_token():
    random_user_id=random.randint(1,query("SELECT COUNT(id) FROM data")[0]["COUNT(id)"])
    response=make_response()
    response.headers["TOKEN"]=base64.standard_b64encode(bytes(json.dumps({
        "id": random_user_id
    }),"utf-8"))
    return response

@app.route('/api/data/<id>')
def get_all_data(id):
    return json.dumps(query(f"SELECT name FROM data WHERE id={id}"))

if __name__=="__main__":
    create_fake_data()