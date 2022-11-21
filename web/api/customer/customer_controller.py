from flask import Blueprint, render_template

from web.models.models import Customer

customer = Blueprint("Single customer view", __name__)


@customer.get("/customers/<string:login>")
def show_customer(login):
    customer = Customer.query.filter(Customer.login == login).first()
    return render_template("customer/index.html", customer=customer)
