from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import users
from flask import flash

class Recipe:
    db = "recipes_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cook_time = data['cook_time']
        self.description = data['description']
        self.instruction = data['instruction']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data["user_id"]
        self.user = None

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for r in results:
            recipes.append(cls(r))
        return results

    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (name, cook_time, description, instruction, user_id) VALUES (%(name)s, %(cook_time)s, %(description)s, %(instruction)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE users SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, cook_time = %(cook_time)s, updated_at = %(updated_at)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        recipe = cls(result[0])
        return recipe

    @classmethod 
    def get_one_recipe_with_user(cls, data):
        query = """
        SELECT * FROM recipes JOIN users
        ON recipes.user_id = users.id
        WHERE recipes.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        print("Random string", results)
        result = results[0]
        recipe = cls(result)
        recipe.user = users.User(
            {
                "id": result['users.id'],
                "first_name": result['first_name'],
                "last_name": result['last_name'],
                "email": result['email'],
                "password": result['password'],
                "created_at": result['users.created_at'],
                "updated_at": result['users.updated_at']
            }
        )
        return recipe

    @classmethod
    def recipes_with_users(cls):
        query = """
            SELECT * FROM recipes JOIN users
            ON recipes.user_id = users.id
        """
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row_from_results in results:
            single_recipe = cls(row_from_results)
            user_data = {
                "id": row_from_results['users.id'],
                "first_name": row_from_results['first_name'],
                "last_name": row_from_results['last_name'],
                "email": row_from_results['email'],
                "password": row_from_results['password'],
                "created_at": row_from_results['users.created_at'],
                "updated_at": row_from_results['users.updated_at']
            }
            single_recipe.user = users.User(user_data)
            recipes.append(single_recipe)
        return recipes

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters")
            is_valid = False
        if len(recipe['instruction']) < 3:
            flash("Instruction must be at least 3 characters")
            is_valid = False
        return is_valid