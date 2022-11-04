from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import recipes
from flask import flash
from flask_bcrypt import Bcrypt 
import re

bcrpyt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("recipes_schema").query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return results

    @classmethod
    def register(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL("recipes_schema").query_db(query, data)

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("recipes_schema").query_db(query, data)
        user = cls(results[0])
        return user

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("recipes_schema").query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # @classmethod
    # def user_with_recipes(cls, data):
    #     query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s;"
    #     results = connectToMySQL("recipes_schema").query_db(query, data)
    #     user = cls(results[0])
    #     for row_from_db in results:
    #         recipe_data = {
    #             "id": row_from_db["recipes.id"],
    #             "name": row_from_db["name"],
    #             "cook_time": row_from_db["cook_time"],
    #             "description": row_from_db["description"],
    #             "instruction": row_from_db["instruction"],
    #             "created_at": row_from_db["recipes.created_at"],
    #             "updated_at": row_from_db["recipes.updated_at"],
    #             "user_id": row_from_db["user_id"]
    #         }
    #         user.recipes.append(recipes.Recipe(recipe_data))
    #     return user


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