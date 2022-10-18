from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success():
    return "Success"


if __name__=="__main__":
    app.run(debug=True)



# from flask import Flask  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response
# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#     app.run(debug=True)    # Run the app in debug mode.

# #This snippet will give back the return if user enters any route that will not work
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return 'NOPE, TRY AGAIN'
