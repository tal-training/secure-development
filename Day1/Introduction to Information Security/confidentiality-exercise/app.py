from flask import Flask, send_file
from faker import Faker
import sqlite3
import json

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
    

@app.route('/api/data')
def get_all_data():
    return json.dumps(query("SELECT * FROM data"))

if __name__=="__main__":
    create_fake_data()