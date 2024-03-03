from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
@app.route("/home" , methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/sales', methods=['GET', 'POST'])
def sale_form():
    return render_template('sale.html')


@app.route("/login", methods=['GET', 'POST'])
def login_form():
    return render_template('login.html')


@app.route("/register", methods=['GET', 'POST'])
def register_form():
    return render_template('register.html')


@app.route("/mission", methods=['GET', 'POST'])
def mission_form():
    return render_template('mission.html')


@app.route("/blog")
def blog_form():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run()
