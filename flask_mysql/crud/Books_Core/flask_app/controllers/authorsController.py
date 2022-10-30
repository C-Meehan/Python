from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.authors import Author 
from flask_app.models.books import Book


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

@app.route('/author/show/<int:id>')
def author_show(id):
    data = {
        "id": id,
    }
    # return render_template("author_show.html", author = Author.get_author_with_books(data), books = Book.get_all_books()) |||This works too just change html
    return render_template("author_show.html", author = Author.get_author_with_books(data), books = Book.not_favorite(data))

@app.route('/add/favorites', methods=['POST'])
def add_favorites():
    data = {
        "author_id": request.form['author_id'],
        "book_id": request.form['book_id']
    }
    Author.add_favorite(data)
    # Author.get_author_with_books(data)
    return redirect(f"/author/show/{request.form['author_id']}")