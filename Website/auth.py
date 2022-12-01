from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])

def login():

    return render_template("login.html")

@auth.route('/registration')

def registration():

    return render_template("registration.html")
