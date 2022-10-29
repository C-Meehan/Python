from flask_app.config.mysqlconnections import connectToMySQL

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
