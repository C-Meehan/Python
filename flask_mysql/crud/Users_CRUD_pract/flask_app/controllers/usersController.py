from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.users import User

@app.route('/')
def index():
    User.get_all
    return render_template('index.html', users = User.get_all())

@app.route("/create", methods=["POST"])
def create():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    id = User.save(data)
    return redirect(f"/show/{id}")

@app.route('/newuser')
def newuser():
    return render_template('/newuser.html')

@app.route("/show/<int:user_id>")
def show(user_id):
    return render_template('show.html', user = User.get_one(user_id))




@app.route('/edit/<int:user_id>')
def edit(user_id):
    return render_template('edit.html', user = User.get_one(user_id))



@app.post("/update/<int:user_id>")
def update(user_id):
    data = {**request.form, "id": user_id}
    User.update(data)
    return redirect(f"/show/{user_id}")

# @app.route("/update/<int:user_id>", methods=["POST"])
# def update(user_id):
#     data = {**request.form, "id": user_id}
#     User.update(data)
#     return redirect(f"/show/{user_id}")

@app.route('/delete/<int:user_id>')
def delete(user_id):
    data = {"id": user_id}
    User.delete(data)
    return redirect('/')