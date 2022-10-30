from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.books import Book
from flask_app.models.authors import Author

@app.route('/books')
def show_books():
    return render_template('books.html', books = Book.get_all_books())

@app.route('/create/books', methods=['POST'])
def create_books():
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    Book.create_books(data)
    return redirect('/books')

@app.route('/book/show/<int:id>')
def book_show(id):
    data = {
        "id": id
    }
    # return render_template("book_show.html", book = Book.get_book_with_authors(data)), authors = Author.get_all())|||This works too just change html
    return render_template("book_show.html", book = Book.get_book_with_authors(data), authors = Author.not_favorite(data))

@app.route('/add/author', methods=['POST'])
def add_fav_author():
    data = {
        "author_id": request.form['author_id'],
        "book_id": request.form['book_id']
    }
    Book.get_fav_book(data)
    return redirect(f"/book/show/{request.form['book_id']}")