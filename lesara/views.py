
from lesara import app, db
from lesara.models import Order
from lesara.utils import predict


@app.route('/')
def index():
    return "main"

@app.route('/predict/<customer_id>')
def get_prediction(customer_id):
    data = Order.query.filter_by(
        customer_id=customer_id).order_by('created_at_date').all()
    results = predict(data)
    return str(results)
