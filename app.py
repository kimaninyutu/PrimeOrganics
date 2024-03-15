from flask import Flask, render_template, request, redirect, session, url_for

from mpesaapi import initiate_session

app = Flask(__name__)
app.secret_key = "kimaninyutu"

credentials = []


@app.route('/')
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/sales', methods=['GET', 'POST'])
def sale_form():
    return render_template('sale.html')


@app.route("/login", methods=['GET', 'POST'])
def login_form():
    return render_template('login.html')


@app.route("/register", methods=['GET', 'POST'])
@app.route("/login/register", methods=['GET', 'POST'])
def register_form():
    return render_template('register.html')


@app.route("/mission", methods=['GET', 'POST'])
def mission_form():
    return render_template('mission.html')


@app.route("/blog")
def blog_form():
    return render_template('blog.html')


@app.route("/test", methods=['POST', 'GET'])
def test():
    if request.method == "POST":
        number = request.form["number"]
        amount = request.form["amount"]
        initiate_session(number, amount)
    return render_template('test.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        number = request.form["number"]
        amount = request.form["amount"]
        username = request.form["username"]
        credentials.append(username)
        credentials.append(amount)
    print(credentials)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
