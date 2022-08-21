import mysql.connector as sql
from flask import Flask, jsonify, make_response, redirect, render_template, request
import database
import pickle


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


@app.route('/login', methods=["POST", "GET"])
def login_validation():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = str(request.form.get('email'))
        password = str(request.form.get('password'))
        if database.check_login(email, password):
            return make_response(render_template('login_success.html', user=email))
        else:
            return redirect("./login")


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    if request.method == "POST":
        name = str(request.form.get('name'))
        email = str(request.form.get('email'))
        password1 = str(request.form.get('password1'))
        password2 = str(request.form.get('password2'))
        if database.check_login(email, password1) == "on user":
            database.signup(email, name, password1)