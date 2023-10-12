from flask_sqlalchemy import SQLAlchemy



class Shopping_list(db.Model):
    def __init__(self, item, app):
        self.item = item
        self.app = app

    db = SQLAlchemy(self.app)
    _id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100))
