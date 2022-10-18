from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')   #Create a dojo route
def dojo():
    return 'Dojo!'

@app.route('/say/<string:phrase>')  #Create a say route with a variable
def phrase(phrase):          #Inputting a word after /say/ will say hello {'phrase'}
    return f'Hi {phrase}!'

@app.route('/repeat/<int:num>/<string:phrase>')
def repeat(num, phrase):
    return f'{phrase * num}'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.