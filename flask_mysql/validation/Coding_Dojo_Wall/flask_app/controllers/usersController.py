from flask_app import app
from flask_app.models.users import User
from flask_app.models.posts import Post
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
    session['id'] = id
    return redirect('/wall')

# @app.route('/login', methods=['POST'])
# def login():
#     data = {"email": request.form['email']}
#     user_in_db = User.get_by_email(data)
#     if not user_in_db:
#         flash("Invalid Email/Password")
#         return redirect("/")
#     if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
#         flash("Invalid Email/Password")
#         return redirect('/')
#     session['id'] = user_in_db.id
#     return redirect('/wall')


@app.route('/login', methods=['POST'])
def login():
    user = User.validate_login(request.form)
    if not user:
        return redirect('/')
    session['id'] = user.id
    return redirect('/wall')



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/wall')
def wall():
    if not session:
        return redirect('/')
    data = {
        "id": session['id']
    }
    return render_template('wall.html', user = User.get_one_user(data), posts = Post.all_posts_with_user())