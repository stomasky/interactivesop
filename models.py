from . import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    SKU = db.Column(db.String(15))
    channel = db.Column(db.String(15))
    SKUchannel = db.Column(db.String(35))
    container = db.Column(db.String(15))
    units_per_container = db.Column(db.Integer)
    box_size = db.Column(db.String(35))
    bag_y_n = db.Column(db.String(3))
    bag_size = db.Column(db.String(25))
    sprayer_cap = db.Column(db.String(25))