from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo


@app.route('/ninja')
def ninja():
    return render_template('/ninjas.html', ninjas = Ninja.get_all(), dojos = Dojo.get_all())


@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    dojo_id = request.form["dojo_id"]
    # data = {
    #     "first_name": request.form["first_name"],
    #     "last_name": request.form["last_name"],
    #     "age": request.form["age"],
    #     "dojo_id": request.form["dojo_id"]
    # }
    Ninja.save(request.form)
    # id = Ninja.save(data)
    return redirect(f'/dojos/{dojo_id}')


@app.route('/delete/<int:id>/<int:dojo_id>')
def delete(id, dojo_id):
    data = {
        "id": id
    }
    Ninja.delete(data)
    return redirect(f'/dojos/{dojo_id}')


@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template('edit.html', ninja = Ninja.get_one(data))

# vvvvvv This will work but not best practice?! vvvvvvv

# @app.route('/update/<int:ninja_id>', methods=['POST'])
# def update(ninja_id):
#     data = {
#         "ninja_id": ninja_id,
#         "first_name": request.form["first_name"],
#         "last_name": request.form["last_name"],
#         "age": request.form["age"]
#     }
#     Ninja.update(data)
#     return redirect(f'/dojos/{request.form["dojo_id"]}')

@app.route('/update/<int:ninja_id>/<int:dojo_id>', methods=['POST'])
def update(ninja_id, dojo_id):
    data = {
        "ninja_id": ninja_id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": dojo_id
    }
    Ninja.update(data)
    return redirect(f'/dojos/{dojo_id}')