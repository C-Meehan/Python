from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "Guess number"

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    if 'attempts' not in session:
        session['attempts'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['Post'])
def guess():
    if (request.form['guess']) != "":
        session['guess'] = int(request.form['guess'])
    if 'attempts' not in session:
        session['attempts'] = 1
    else:
        session['attempts'] += 1
    return redirect('/')

@app.route('/correct')
def correct():
    return render_template('copy.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
