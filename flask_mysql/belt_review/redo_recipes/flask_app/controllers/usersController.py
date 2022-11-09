from flask_app import app
from flask_app.models.users import User
from flask_app.models.recipes import Recipe
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("login.html", users = User.get_all_users())

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        session["first_name"] = request.form['first_name']
        session["last_name"] = request.form['last_name']
        session["email"] = request.form['email']
        return redirect('/')
    secret = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": secret
    }
    id = User.register(data)
    session["id"] = id
    return redirect('/homepage')

@app.route('/login', methods=['POST'])
def login():
    user = User.validate_login(request.form)
    if not user:
        return redirect('/')
    session['id'] = user.id
    return redirect('/homepage')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/homepage')
def homepage():
    if not session:
        return redirect('/')
    data = {
        "id": session["id"]
    }
    return render_template("homepage.html", user = User.get_one_user(data), recipes = Recipe.recipes_with_users())