from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo

@app.route('/ninja')
def ninja():
    return render_template('/ninjas.html', ninjas = Ninja.get_all(), dojos = Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    id = Ninja.save(data)
    return redirect(f'/dojos/{data["dojo_id"]}')

@app.route('/delete/<int:id>/<int:dojo_id>')
def delete(id, dojo_id):
    data = {
        "id": id
    }
    Ninja.delete(data)
    return redirect(f'/dojos/{dojo_id}')