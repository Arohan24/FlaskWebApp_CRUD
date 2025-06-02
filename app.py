
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MongoUsername = os.getenv("MongoDB_Username")
MongoPassword = os.getenv("MongoDB_Password")
AppSecret = os.getenv("App_Secret")

app = Flask(__name__)
app.secret_key = AppSecret

MONGO_URI = f"mongodb+srv://{MongoUsername}:{MongoPassword}@flaskwebcluster.qmybnkb.mongodb.net/?retryWrites=true&w=majority&appName=FlaskWebCluster"
client = MongoClient(MONGO_URI)
db = client["testdb"]
collection = db["formdata"]

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        if not name or not email:
            flash("All fields are required!")
            return render_template("form.html")

        collection.insert_one({"name": name, "email": email})
        return redirect(url_for('success'))

    except Exception as e:
        flash(f"Error: {str(e)}")
        return render_template("form.html")

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/view')
def view():
    all_data = list(collection.find())
    return render_template("view.html", data=all_data)

if __name__ == '__main__':
    app.run(debug=True)
