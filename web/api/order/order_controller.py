from flask import Blueprint, render_template

from web.models.models import Order

order = Blueprint("Single order view", __name__)


@order.get("/orders/<string:id>")
def show_order(id):
    order = Order.query.filter(Order.order_id == id).first()
    return render_template("order/index.html", order=order)
