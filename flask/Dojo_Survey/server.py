# Collaborated with Jang Sing

from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "password"

@app.route('/')
def index():
    print(type(session))
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    if (request.form['name']) != "":
        session['name'] = request.form['name']
    if (request.form['email']) != "":
        session['email'] = request.form['email']
    if (request.form['location']) != "":
        session['location'] = request.form['location']
    if 'language' in request.form:
        session['language'] = request.form['language']
    if (request.form['comment']) != "":
        session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def submission():
    return render_template('submit.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)