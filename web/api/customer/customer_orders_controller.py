from flask import Blueprint, render_template

from web.models.models import Customer

customer_orders = Blueprint("Customer orders view", __name__)


@customer_orders.get("/customers/<string:login>/orders")
def show_customer_orders(login):
    customer = Customer.query.filter(Customer.login == login).first()
    return render_template("customer_order/index.html", customer=customer)
