from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
from flask import render_template, request

from mongoengine import Document, IntField, StringField


app = Flask(__name__)

def get_db():
    client = MongoClient(host='yoga_spot',
                         port=27017, 
                         username='root', 
                         password='football',
                        )
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



class User(Document):
    user_id = IntField(unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = StringField(max_length=30, unique=True)
    password = StringField()


@app.route("/users")
def user():
    # User(user_id=1, first_name="Christian", last_name="Hur", email="christian@uta.com", password="abc1234").save()
    # User(user_id=2, first_name="Mary", last_name="Jane", email="mary.jane@uta.com", password="password123").save()
    users = User.objects.all()
    return render_template("user.html", users=users)

@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    if request.method == "POST":
        id = request.form.get('classID')
        title = request.form.get('title')
        instructor = request.form.get('instructor')

        # Save the enrollment data or perform any other actions

        return render_template("enrollment.html", enrollment=True, data={"id": id, "title": title, "instructor": instructor})

    # Handle GET request to render the form
    return render_template("enrollment.html", enrollment=False)


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
