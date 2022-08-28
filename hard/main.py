from curses.ascii import islower, isupper
from flask import Flask, make_response, redirect, render_template, request
import database


app = Flask(__name__)


@app.errorhandler(403)
def error_403(e):
    return render_template('error_handler.html', error = "ERROR 403 - ACCESS FORBIDDEN")

@app.errorhandler(404)
def error_404(e):
    return render_template('error_handler.html', error = "ERROR 404 - PAGE NOT FOUND")


@app.errorhandler(500)
def error_500(e):
    return render_template('error_handler.html', error = "ERROR 500 - INTERNAL SERVER ERROR")

@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/login', methods=["POST", "GET"])
def login_validation():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = str(request.form.get('username'))
        password = str(request.form.get('password'))
        if database.check_login(username, password)[0]:
            return "Welcome {}".format(username)
            return make_response(render_template('login_success.html', user=username))
        else:
            return "wrong credentials... <br> please go back and try logining in again or signup if you are new"


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    if request.method == "POST":
        username = str(request.form.get('username'))
        #email = str(request.form.get('email'))
        password1 = str(request.form.get('password1'))
        password2 = str(request.form.get('password2'))
        if password1 != password2:
            return "passwords do not match<br>go back and try again"
        count = [0, 0, 0, 0]
        for i in password1:
            if i.islower():
                count[0] += 1
            if i.isupper():
                count[1] += 1
            if i.isdigit():
                count[2] += 1
            if i in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", "{", "}", ";", ":", "\'", "\"", ",", ".", "/", "?", "<", ">"]:
                count[3] += 1
        if count[0] < 1 or count[1] < 1 or count[2] < 1 or count[3] < 1 or sum(count) <= 8:
            return "password conditions not met<br>password must contain atleast 1 lowercase letter, 1 uppercase latter, 1 digit and 1 symbol and length should be atleast 8"
        if database.check_user(username):
            return 'user already exists<br>please go back and try a different username'
        else:
            database.signup(username, password1, password2)
            return 'account created successfully<br>now go back and login'




if __name__ == '__main__':
    app.run(port='8080')