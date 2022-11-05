from flask_app import app
from flask_app.models.posts import Post
from flask_app.models.users import User
from flask import render_template, redirect, request, session, flash

@app.route('/create/post', methods=['POST'])
def create_post():
    if not Post.validate_post(request.form):
        return redirect('/wall')
    data = {
        "content": request.form['content'],
        "user_id": request.form['user_id']
    }
    Post.create_post(data)
    return redirect('/wall')

@app.route('/delete/post/<int:id>')
def delete_post(id):
    data = {
        "id": id
    }
    Post.delete_post(data)
    return redirect('/wall')
