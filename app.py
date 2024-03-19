import functools
import os
import secrets

from flask import Flask, render_template, request, redirect, session, url_for, flash
from passlib.hash import pbkdf2_sha256 as pbk
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = f"{secrets.token_urlsafe()}"
client = MongoClient(os.environ.get("MONGO_URI"))

db = client.users  # DATABASE NAME
users = db.users  # COLLECTION NAME


def login_required(route):
    @functools.wraps(route)
    def wrap(*args, **kwargs):
        if not session.get("email"):
            return redirect(url_for("login"))
        return route(*args, **kwargs)

    return wrap


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', email=session.get("email"))


@app.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", greeting="Hello " + session.get("name"))


@app.route('/sales', methods=['GET', 'POST'])
@login_required
def sale():
    return render_template('sale.html', greeting="Hello " + session.get("name"))


@app.route("/login", methods=['GET', 'POST'])
def login():
    email = ""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = users.find_one({'email': email})
            if user and pbk.verify(password, user['password']):
                session['email'] = email
                session['name'] = user['name']
                return redirect(url_for('home'))
            else:
                flash('Invalid email or password. Please try again or sign up.')
        except Exception as e:
            flash('Error while trying to login: {}'.format(e))
    return render_template('login.html', email=email)


@app.route("/mission", methods=['GET', 'POST'])
@login_required
def mission():
    return render_template('mission.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user_data = {"name": name, "email": email, "password": pbk.hash(password)}
        users.insert_one(user_data)
        print(users)
        session['email'] = email
        session['name'] = name
        flash("Your account has been created successfully")
        return redirect(url_for("login"))

    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
