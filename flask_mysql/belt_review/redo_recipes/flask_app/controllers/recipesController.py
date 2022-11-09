from flask_app import app
from flask_app.models.recipes import Recipe
from flask_app.models.users import User
from flask import render_template, redirect, request, session, flash

@app.route('/new/recipe')
def new_recipe():
    if not session:
        return redirect('/')
    return render_template("newRecipe.html")

@app.route('/create/recipe', methods=["POST"])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        session['name'] = request.form['name']
        session['description'] = request.form['description']
        session['instruction'] = request.form['instruction']
        return redirect('/new/recipe')
    data = {
        "user_id": session['id'],
        "name": request.form['name'],
        "cook_time": request.form['cook_time'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
    }
    Recipe.create_recipe(data)
    return redirect('/homepage')

@app.route('/delete/recipe/<int:id>')
def delete_recipe(id):
    data = {
        "id": id
    }
    Recipe.delete_recipe(data)
    return redirect('/homepage')

@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    if not session:
        return redirect('/')
    data = {
        "id": id
    }
    return render_template("editRecipe.html", recipe = Recipe.get_one_recipe(data))

@app.route('/update/recipe', methods=['POST'])
def update_id():
    if not Recipe.validate_recipe(request.form):
        session['name'] = request.form['name']
        session['description'] = request.form['description']
        session['instruction'] = request.form['instruction']
        return redirect(f"/edit/recipe/{request.form['recipe_id']}")
    data = {
        "recipe_id": request.form['recipe_id'],
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "cook_time": request.form['cook_time'],
    }
    Recipe.update_recipe(data)
    return redirect('/homepage')

@app.route('/show/recipe/<int:id>')
def show_recipe(id):
    if not session:
        return redirect('/')
    data = {
        "id": id
    }
    session_data = {
        "id": session['id']
    }
    return render_template('showRecipe.html', user= User.get_one_user(session_data), recipe = Recipe.get_one_recipe_with_user(data))