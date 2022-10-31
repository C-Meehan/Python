from flask_app import app
from flask_app.models.users import User
from flask import render_template, redirect, request, session

@app.route('/')
def users():
    session.clear()
    return render_template('users.html', users = User.get_all())

@app.route('/newuser')
def newuser():
    return render_template('createUser.html')

@app.route('/create', methods=['POST'])
def save():
    email_in_db = User.check_emails(request.form['email'])
    if email_in_db:
        email_is_unique = False
    else:
        email_is_unique = True

    if not User.validate_user(request.form, email_is_unique):
        session["first_name"] = request.form["first_name"]
        session["last_name"] = request.form["last_name"]
        session["email"] = request.form["email"]
        return redirect('/newuser')
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    id = User.save(data)
    session.clear()
    return redirect(f'/show/{id}')
    # data = {request.form}
    # User.save(data)
    # return redirect('/')

@app.route('/show/<int:id>')
def show(id):
    data = {'id':id}
    return render_template('show.html', user = User.get_one(data))

@app.route('/edit/<int:id>')
def edit(id):
    data = {'id': id}
    user = User.get_one(data)
    if "first_name" not in session:
        session['first_name'] = user.first_name 
    if "last_name" not in session:
        session['last_name'] = user.last_name
    return render_template('edit.html', user = user)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        # 'email': request.form['email']
    }
    if not User.validate_user_update(request.form):
        session["first_name"] = request.form["first_name"]
        session["last_name"] = request.form["last_name"]
        # session["email"] = request.form["email"]
        return redirect(f'/edit/{id}')
    print("B")
    user = User.update(data)
    session.pop('first_name')
    session.pop('last_name')
    return redirect(f'/show/{id}')

@app.route('/delete/<int:id>')
def delete(id):
    data = {'id': id}
    User.delete(data)
    return redirect('/')