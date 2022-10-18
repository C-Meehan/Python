from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", row = 8, col = 8, color1 = "red", color2 = "black")
    #display 8 by 8 checkerboard

@app.route('/<int:num1>')
def four(num1):
    return render_template("index.html", row = num1, col = 8, color1 = "red", color2 = "black")
    #display 8 by 4 checkerboard

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def custom(num1, num2, color1, color2):
    return render_template("index.html", row = num1, col = num2, color1 = color1, color2 = color2)
    #display checkerboard based off arguments passed

if __name__=="__main__":
    app.run(debug=True)