from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shopping_list.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Shopping_list(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100))

    def __init__(self, item):
        self.item = item


@app.route('/add-new-item', methods = ['POST'])
def add_new_item():
    print("add new item")
    data = request.json
    itm = Shopping_list(data["item"])
    db.session.add(itm)
    db.session.commit()
    return redirect("/")

@app.route('/')
def index():
    return render_template('index.html', shopping_list=Shopping_list.query.all())


@app.route('/delete/<string:id>')
def delete(id):
    print(id)
    Shopping_list.query.filter_by(_id=id).delete()
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()


    app.run(debug=True)
