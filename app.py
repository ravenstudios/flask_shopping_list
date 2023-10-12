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



@app.route('/')
def index():
    return render_template('index.html', shopping_list=Shopping_list.query.all())



@app.route('/add-new-item', methods = ['POST'])
def add_new_item():
    db.session.add(Shopping_list(request.json["item"]))
    db.session.commit()
    return redirect("/")



@app.route('/delete-item', methods = ['POST'])
def delete():
    Shopping_list.query.filter_by(_id=request.json["id"]).delete()
    db.session.commit()
    return redirect("/")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    # app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
