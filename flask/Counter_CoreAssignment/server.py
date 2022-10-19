# Collaborated with Jang Sing

from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'secrets are key'

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = 0
    else:
        session['num'] += 1

    if 'visited' not in session:
        session['visited'] = 0
    else:
        session['visited'] += 1

    return render_template('index.html')

@app.route('/add')
def add():
    session['num'] += 1
    return redirect('/')

@app.route('/destroy_count')
def destroy_count():
    session['num'] = -1
    return redirect ("/")

@app.route('/destroy_session')
def destroy():
    session.clear()
    session['num'] = -1
    return redirect("/")

@app.route('/form', methods=['Post'])
def input():
    request.form
    print(request.form)
    newval = request.form['Amount']
    session['num'] += (int(newval)-1)
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)