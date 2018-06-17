from lesara import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(32))
    order_id = db.Column(db.Integer)
    order_item_id = db.Column(db.Integer)
    num_items = db.Column(db.Integer)
    revenue = db.Column(db.Float)
    created_at_date = db.Column(db.DateTime)
    
    def __init__(self, customer_id, order_id, order_item_id, num_items, revenue, created_at_date):
        self.customer_id = customer_id
        self.order_id = order_id
        self.order_item_id = order_item_id
        self.num_items = num_items
        self.revenue = revenue
        self.created_at_date = created_at_date

    def __repr__(self):
        return 'Order %s' % self.order_id

