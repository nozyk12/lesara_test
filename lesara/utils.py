from datetime import date, datetime, timedelta

import dill
import numpy


with open('/app/model.dill', 'rb') as f:
    obj = dill.load(f)
    predict_lesara = obj.predict


def calculate_coefficients(data):

    until_day = datetime(year=2017, month=10, day=17)

    max_items = 0
    max_revenue = 0
    total_revenue = 0
    total_orders = len(data)
    last_created_at_date = None
    longest_interval = 0

    for d in data:
        if d.num_items > max_items:
            max_items = d.num_items

        if d.revenue > max_revenue:
            max_revenue = d.revenue

        total_revenue += d.revenue

        if last_created_at_date is not None:
            interval = (d.created_at_date - last_created_at_date).days
            if interval > longest_interval:
                longest_interval = interval

        last_created_at_date = d.created_at_date

    days_since_last_order = int((until_day - last_created_at_date).days)
    longest_interval = int(longest_interval)

    # sorry, I don't understand why yours predict method takes two dimensional array
    return numpy.array([
        [max_items, max_revenue, total_revenue,
            days_since_last_order, longest_interval, total_orders],
        [0]*6]
    )


def predict(data):
    coefficients = calculate_coefficients(data)
    return predict_lesara(coefficients)
