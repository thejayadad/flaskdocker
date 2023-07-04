from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
from flask import render_template, request


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

@app.route('/classes/')
@app.route('/classes/<term>')
def classes(term="Summer"):
    classData = [{"classID":"101","title":"Hot Yoga","instructor":"Jace The Goat", "duration":"30"},
    {"classID":"102","title":"Meditation Yoga","instructor":"Jada Boo", "duration":"60"},
    {"classID":"103","title":"Flexible Yoga","instructor":"Flexin With Jazz", "duration":"75"},
    {"classID":"104","title":"Healing Yoga","instructor":"Jack Rabbit", "duration":"45"}]
    return render_template("./classes.html", classData=classData, term=term)

@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id= request.args.get('classID')
    title= request.args.get('title')
    instructor= request.args.get('instructor')
    return render_template("enrollment.html", enrollment=True, data={"id":id, "title":title,"instructor":instructor})




if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
