from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import books

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL("books_schema").query_db(query)
        authors = []
        for a in results:
            authors.append(cls(a))
        return authors

    @classmethod
    def create(cls, data):
        query = "INSERT INTO authors (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL("books_schema").query_db(query, data)

    @classmethod
    def get_one_author(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL("books_schema").query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_author_with_books(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL("books_schema").query_db(query, data) 
        author = cls(results[0])
        for row in results:
            if row['books.id'] == None:
                break
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorites.append(books.Book(data))
        return author

    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL("books_schema").query_db(query, data)

    @classmethod
    def not_favorite(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN (SELECT author_id FROM favorites WHERE book_id = %(id)s);"
        results = connectToMySQL("books_schema").query_db(query, data)
        print(results)
        non_fav_authors = []
        for a in results:
            non_fav_authors.append(cls(a))
        return non_fav_authors