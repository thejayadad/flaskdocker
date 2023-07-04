from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
from flask import render_template


app = Flask(__name__)

def get_db():
    client = MongoClient(host='yoga_spot',
                         port=27017, 
                         username='root', 
                         password='football',
                        authSource="admin")
    db = client["yoga_spot"]
    return db

@app.route('/')
def index():
    return render_template("./index.html", login=False)

@app.route('/login')
def login():
    return render_template("./login.html", login=False)

@app.route('/classes')
def classes():
    return render_template("./classes.html", login=False)


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
