from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import users
from flask import flash

class Post:
    db = "dojo_wall_schema"
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM posts;"
        results = connectToMySQL(cls.db).query_db(query)
        posts = []
        for p in results:
            posts.append(cls(p))
        return results

    @classmethod
    def create_post(cls, data):
        query = "INSERT INTO posts (content, user_id) VALUES (%(content)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete_post(cls, data):
        query = "DELETE FROM posts WHERE posts.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def one_post_with_user(cls, data):
        query = """
        SELECT * FROM posts JOIN users
        ON posts.user_id = users.id
        WHERE posts.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        result = results[0]
        post = cls(result)
        post.user = users.User(
            {
                "id": result["users.id"],
                "first_name": result["first_name"],
                "last_name": result["last_name"],
                "email": result["email"],
                "password": result["password"],
                "created_at": result["users.created_at"],
                "updated_at": result["users.updated_at"],
            }
        )
        return post



    @classmethod
    def all_posts_with_user(cls):
        query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id ORDER BY posts.created_at DESC;"
        results = connectToMySQL(cls.db).query_db(query)
        posts = []
        print(results)
        for row_from_results in results:
            single_post = cls(row_from_results)
            user_data = {
                "id": row_from_results["users.id"],
                "first_name": row_from_results["first_name"],
                "last_name": row_from_results["last_name"],
                "email": row_from_results["email"],
                "password": row_from_results["password"],
                "created_at": row_from_results["users.created_at"],
                "updated_at": row_from_results["users.updated_at"],
            }
            single_post.user = users.User(user_data)
            posts.append(single_post)
            print("posts", posts)
        return posts


    @staticmethod
    def validate_post(post):
        is_valid = True
        # query = "SELECT * FROM posts WHERE id = %(id)s;"
        # result = connectToMySQL("dojo_wall_schema").query_db(query, post)
        if len(post['content']) < 1:
            flash("Post not allowed. Content must be present.")
            is_valid = False
        return is_valid