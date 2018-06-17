from lesara import db

class Order(db.Model):
    customer_id = db.Column(db.String(32), unique=True, nullable=False)
    order_id = db.Column(db.Integer, primary_key=True)
    order_item_id = db.Column(db.Integer)
    num_items = db.Column(db.Integer)
    revenue = db.Column(db.Float)
    created_at_date = db.Column(db.DateTime)

    def __repr__(self):
        return 'Order %s' % self.order_id

