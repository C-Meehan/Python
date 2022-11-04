from flask_app import app
from flask_app.controllers import usersController, recipesController

# ADD additional controller name ^^^^^^^^^

if __name__ == "__main__":
    app.run(debug=True)