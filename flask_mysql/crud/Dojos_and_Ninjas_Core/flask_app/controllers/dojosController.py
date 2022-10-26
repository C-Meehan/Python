from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojos import Dojo 

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def home():
    return render_template('dojo.html', dojos = Dojo.get_all())

@app.route('/create/dojo', methods=['POST'])
def create():
    data = {
        "name": request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show(dojo_id):
    data = {
        "id": dojo_id
    }
    return render_template('ninjas_in_dojos.html', dojo = Dojo.get_dojo_with_ninjas(data))