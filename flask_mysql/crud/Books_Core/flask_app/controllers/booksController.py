from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.books import Book

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