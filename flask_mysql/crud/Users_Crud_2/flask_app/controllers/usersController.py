from flask_app import app
from flask_app.models.users import User
from flask import render_template, redirect, request

@app.route('/')
def users():
    return render_template('users.html', users = User.get_all())

@app.route('/newuser')
def newuser():
    return render_template('createUser.html')

@app.route('/create', methods=['POST'])
def save():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    id = User.save(data)
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
    return render_template('edit.html', user = User.get_one(data))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    user = User.update(data)
    return redirect(f'/show/{id}', user = user)

@app.route('/delete/<int:id>')
def delete(id):
    data = {'id': id}
    User.delete(data)
    return redirect('/')