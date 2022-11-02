from flask_app import app
from flask_app.models.orders import Order
from flask import render_template, redirect, request, session

@app.route('/')
def index():
    return render_template('cookies.html', orders = Order.get_all())

@app.route('/new/order')
def new_order():
    return render_template('newOrder.html')

@app.route('/place/order', methods=['POST'])
def place_order():
    if not Order.validate_order(request.form):
        return redirect('/new/order')
    data = {
        "name": request.form['name'],
        "cookie_type": request.form['cookie_type'],
        "num_of_boxes": request.form['num_of_boxes']
    }
    Order.new_order(data)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit_order(id):
    data = {
        "id":id
    }
    return render_template('edit.html', order = Order.get_one(data))

@app.route('/update/order/<int:id>', methods=['POST'])
def update_order(id):
    if not Order.validate_order(request.form):
        return redirect(f'/edit/{id}')
    data = {
        'id': id,
        'name': request.form['name'],
        'cookie_type': request.form['cookie_type'],
        'num_of_boxes': request.form['num_of_boxes']
    }
    order = Order.update_order(data)
    return redirect('/')