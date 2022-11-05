from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "dojo_wall_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posts = []

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return results

    @classmethod
    def register(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        user = cls(results[0])
        return user












    @staticmethod
    def validate_registration(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("recipes_schema").query_db(query,user)
        if len(result) >= 1:
            flash("Email already in use. Try Again")
            is_valid = False
        if not user['first_name'].isalpha() or len(user['first_name']) < 2:
            flash("Must use alphabetical letters only/Name must be at least 2 characters long")
            is_valid = False
        if not user['last_name'].isalpha() or len(user['last_name']) < 2:
            flash("Must use alphabetical letters only/Name must be at least 2 characters long")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must contain at least 8 characters")
            is_valid = False
        if user['password'] != user['confirm-password']:
            flash("Password does not match")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        # is_valid = True
        if not user["email"]:
            flash("Invalid Email/Password")
            return False
        user_in_db = User.get_by_email(user)
        if not user_in_db:
            flash("Invalid Email/Password")
            return False
        if not bcrypt.check_password_hash(user_in_db.password, user['password']):
            flash("Invalid Email/Password")
            return False
        # return is_valid
        return user_in_db
