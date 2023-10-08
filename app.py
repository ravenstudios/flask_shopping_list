from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__, static_url_path='/static')



shopping = ["Milk", "Eggs", "Soap", "Cicken", "Cheese", "Salsa", "Cookies", "Dog Food"]
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', shopping_list=shopping_list)

@app.route('/')
def index():
    return render_template('index.html', shopping_list=shopping)

@app.route('/add_new_item', methods = ['POST'])
def add_new_item():
    print("add new item")
    return render_template('index.html', shopping_list=shopping)
