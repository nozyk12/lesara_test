from flask import Response

from lesara import app, db
from lesara.models import Order
from lesara.utils import predict


@app.route('/')
def index():
    msg = """
    Welcome to main page of Customer Lifetime Value Project.
    Please use an endpoint /predict/customer_id to get predicted CLV value.
    """
    return Response(msg, status=200)


@app.route('/predict/<customer_id>')
def get_prediction(customer_id):
    data = Order.query.filter_by(
        customer_id=customer_id).order_by('created_at_date').all()
    if len(data) == 0:
        return Response("Did not found orders for given customer", status=404)
    clv = predict(data)

    response = str([customer_id, str(clv)])
    return Response(response, status=200)
