from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

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
def ping_server():
    return "Welcome to the Yoga Spot."


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)