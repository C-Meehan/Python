from flask_app import app
from flask import render_template, request, redirect, session

@app.route('/')
def hello_world():
  return 'Hello... World.'

@app.route('/home')
def dashboard():
  return 'Houston we have a problem.'

@app.route('/say/<name>')
def hello(name):
  print(type(name))
  # int(name)
  # print(type(int(name)))
  return "Hi " + name + "!"

@app.route('/sayformatted/<name>')
def hello_formatted(name):
  print(type(name))
  # int(name)
  # print(type(int(name)))
  return f"Hi {name}!"

@app.route('/sayagain/<word>/<int:num>')
def hello_again(word, num):
  print(num)
  # print(type(num))
  # return word * int(num)
  return f"{word * num}"

@app.route('/repeat')
def passingData():
  return render_template("index.html", phrase="Houston, we have a problem", times=5)


@app.route('/lists')
def renderLists():
  studentInfo = [
        {'name' : 'Timmy Jimmy-Jam', 'age' : 35},
        {'name' : 'Ben Jammin', 'age' : 30 },
        {'name' : 'Test McTesterson', 'age' : 25},
        {'name' : 'DB Cooper', 'age' : 85}
    ]
  return render_template('lists.html', 
    students=studentInfo, 
    list=[3,4,5,6,5,7,8,9,5,4,3,2,5,67,7,8])

@app.route('/index/<word>/<color>/<othercolor>')
def root(word,color,othercolor):
  return render_template('index.html', 
    phrase = word, 
    num=8, 
    color = color,
    color2 = othercolor)