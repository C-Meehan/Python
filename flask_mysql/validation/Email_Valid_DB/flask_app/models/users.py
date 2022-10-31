from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("user_crud_2_schema").query_db(query)
        users = []
        for i in users:
            users.append(cls(i))
        return results

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL("user_crud_2_schema").query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s WHERE id = %(id)s;"
        return connectToMySQL("user_crud_2_schema").query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL("user_crud_2_schema").query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("user_crud_2_schema").query_db(query, data)
        user = cls(results[0])
        return user

    @classmethod
    def check_emails(cls, data):
        query = "SELECT email FROM users WHERE email = %(email)s;"
        data = {
            "email": data
        }
        result = connectToMySQL('user_crud_2_schema').query_db(query, data)
        return result

    @staticmethod
    def validate_user(user, email_is_unique):
        is_valid = True
        if not user['first_name'].isalpha():
            flash("Must fill out field")
            is_valid = False
        if len(user['last_name']) <= 0:
            flash("Must fill out field")
            is_valid = False
        if not email_is_unique:
            flash("Duplicate Email not allowed")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_user_update(user):
        is_valid = True
        if not user['first_name'].isalpha():
            flash("Must fill out field")
            is_valid = False
        if len(user['last_name']) <= 0:
            flash("Must fill out field")
            is_valid = False
        return is_valid
            
