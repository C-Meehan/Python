from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user
from datetime import datetime
dtformat = "%m/%d/%Y %I:%M %p"

@app.route('/allthethings')
def allthethings():
  return render_template('showquery.html', 
  users = user.User.getAll(),
  timeStampFormat = dtformat)

@app.route('/logout')
def sessionreset():
  session.clear()
  return redirect('/theshow')