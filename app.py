import os
import secrets

from flask import Flask, render_template, request, redirect, session, url_for, abort, flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = f"{secrets.token_urlsafe()}"
client = MongoClient(os.environ.get("mongodb+srv://kimanihezekiah:<password>@cluster0.atrb87s.mongodb.net/"))

users = client.get_default_database("users")


@app.route('/')
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html', email=session.get("email"))


@app.route("/home", methods=['GET', 'POST'])
def home():
    if not session.get("email"):
        abort(401)
    return render_template("home.html", greeting="Hello " + session.get("name"))


@app.route('/sales', methods=['GET', 'POST'])
def sale_form():
    return render_template('sale.html')


@app.route("/login", methods=['GET', 'POST'])
def login_form():
    email = ""
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            for user in users:
                if user["email"] == email and user["password"] == password:
                    session['email'] = email
                    session["name"] = user["name"]
                    return redirect(url_for('home'))
        except:
            flash("Something went wrong while trying to login")
        flash("Invalid credentials")
    return render_template('login.html', email=email)


@app.route("/mission", methods=['GET', 'POST'])
def mission_form():
    return render_template('mission.html')


@app.route("/blog")
def blog_form():
    return render_template('blog.html')


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user_data = {"name": name, "email": email, "password": password}
        users.append(user_data)
        print(users)
        session['email'] = email
        session['name'] = name
        flash("Your account has been created successfully")
        return redirect(url_for("login_form"))

    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
