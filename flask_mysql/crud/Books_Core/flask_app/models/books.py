from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import authors

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []

    @classmethod
    def get_all_books(cls):
        query = 'SELECT  * FROM books'
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for b in results:
            books.append(cls(b))
        return books

    @classmethod
    def create_books(cls,data):
        query = 'INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);'
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def not_favorite(cls, data):
        query = "SELECT * FROM books WHERE books.id NOT IN (SELECT book_id FROM favorites WHERE author_id = %(id)s);"
        results = connectToMySQL("books_schema").query_db(query, data)
        print(results)
        non_fav_books = []
        for b in results:
            non_fav_books.append(cls(b))
        return non_fav_books

    @classmethod
    def get_one_book(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL("books_schema").query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_book_with_authors(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL("books_schema").query_db(query, data)
        book = cls(results[0])
        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.favorites.append(authors.Author(data))
        return book

    @classmethod
    def get_fav_book(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL("books_schema").query_db(query, data)