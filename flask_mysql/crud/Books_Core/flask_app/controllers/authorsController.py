from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.authors import Author 

@app.route('/')
def index():
    return render_template("authors.html", authors = Author.get_all())

@app.route('/create/author', methods=['POST'])
def create():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name']
    }
    Author.create(data)
    return redirect('/')