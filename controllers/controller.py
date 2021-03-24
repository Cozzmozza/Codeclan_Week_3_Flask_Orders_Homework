from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Order Status', orders=orders)

@app.route('/orders/<index>')
def show(index):
    return render_template('order.html', order=orders[int(index)])