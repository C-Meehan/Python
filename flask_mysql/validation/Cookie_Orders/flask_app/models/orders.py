from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL("cookie_orders").query_db(query)
        orders = []
        for o in orders:
            orders.append(cls(o))
        return results

    @classmethod
    def new_order(cls, data):
        query = "INSERT INTO orders (name, cookie_type, num_of_boxes) VALUES (%(name)s, %(cookie_type)s, %(num_of_boxes)s);"
        return connectToMySQL("cookie_orders").query_db(query, data)

    @classmethod
    def update_order(cls, data):
        query = "UPDATE orders SET name = %(name)s, cookie_type = %(cookie_type)s, num_of_boxes = %(num_of_boxes)s WHERE id = %(id)s;"
        return connectToMySQL("cookie_orders").query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        results = connectToMySQL("cookie_orders").query_db(query, data)
        order = cls(results[0])
        return order

    @staticmethod
    def validate_order(order):
        print("Order formssssss", order)
        is_valid = True
        if not order['name'].isalpha() or len(order['name']) < 2:
            flash("Invalid name/Must be at least 2 characters long")
            is_valid = False
        # if len(order['name']) < 2:
        #     flash("Invalid name/Must be at least 2 characters long")
        #     is_valid = False
        if len(order['num_of_boxes']) < 1:
            flash("Must order at least 1 box")
            is_valid = False
        elif int(order['num_of_boxes']) < 0:
            flash("Must order at least 1 box")
            is_valid = False
        return is_valid
