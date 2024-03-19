import functools

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from passlib.hash import pbkdf2_sha256 as pbk

pages = Blueprint('primeorganics', __name__, template_folder='templates', static_folder='static')


def login_required(route):
    @functools.wraps(route)
    def wrap(*args, **kwargs):
        if not session.get("email"):
            return redirect(url_for("primeorganics.login"))
        return route(*args, **kwargs)

    return wrap


@pages.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', email=session.get("email"))


@pages.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", greeting="Hello " + session.get("name"))


@pages.route('/sales', methods=['GET', 'POST'])
@login_required
def sale():
    return render_template('sale.html', greeting="Hello " + session.get("name"))


@pages.route("/login", methods=['GET', 'POST'])
def login():
    email = ""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = current_app.db.users.find_one({'email': email})
            if user and pbk.verify(password, user['password']):
                session['email'] = email
                session['name'] = user['name']
                return redirect(url_for('primeorganics.home'))
            else:
                flash('Invalid email or password. Please try again or sign up.')
        except Exception as e:
            flash('Error while trying to login: {}'.format(e))
    return render_template('login.html', email=email)


@pages.route("/mission", methods=['GET', 'POST'])
@login_required
def mission():
    return render_template('mission.html')


@pages.route("/blog")
@login_required
def blog():
    return render_template('blog.html')


@pages.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user_data = {"name": name, "email": email, "password": pbk.hash(password)}
        current_app.db.users.insert_one(user_data)
        session['email'] = email
        session['name'] = name
        flash("Your account has been created successfully")
        return redirect(url_for("primeorganics.login"))

    return render_template('signup.html')


@pages.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('primeorganics.index'))
