from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.items import User


@app.route('/')
def index():
    User.get_all
    return render_template('index.html', users = User.get_all())

@app.route('/create', methods=['POST'])
def create():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/')

@app.route('/newuser')
def newuser():
    return render_template('/newuser.html')