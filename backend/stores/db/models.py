from backend import db

class Item(db.Model):
    id = db.Column(db.String(60), primary_key=True, unique=True)
    name = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float(asdecimal=True), nullable=False)
    store_id = db.Column(db.String(60), db.ForeignKey('store.id'), nullable=False)

class Store(db.Model):
    id = db.Column(db.String(60), primary_key=True, unique=True)
    name = db.Column(db.String(60), nullable=False)
    items = db.relationship('Item', backref='store', lazy=True)