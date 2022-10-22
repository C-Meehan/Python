from flask_app import app
from flask import render_template, request, redirect, session

@app.route('/theform')
def formRender():
  # print(f"Get Route: {request.form}")
  return render_template('form.html')

@app.route('/form', methods=['post'])
def formPost():
  print(f"Post Route: {request.form}")
  if request.form['purpose'] == 'register':
    session['username'] =  request.form['name']
    session['useremail'] =  request.form['email']
  elif request.form['purpose'] == 'login':
    session['userpassword'] =  request.form['password']
    session['useremail'] =  request.form['email']
  return redirect('/form', methods=['post'])

@app.route('/theshow')
def formDisplay():
  # print(session['username'])
  # print(session['useremail'])
  return render_template('show.html')