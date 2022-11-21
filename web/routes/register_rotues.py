from flask import Flask

from web.api.complaint.complaint_controller import complaint
from web.api.credit_card.edit_card_controller import edit_card
from web.api.customer.customer_controller import customer
from web.api.customer.customer_orders_controller import customer_orders
from web.api.driver.driver_controller import driver
from web.api.first_query.first_query_controller import first_query_native, first_query_orm
from web.api.order.order_controller import order
from web.api.second_query.second_query_controller import second_query_orm, second_query_native


def register_routes(app: Flask) -> None:
    app.register_blueprint(first_query_native)
    app.register_blueprint(first_query_orm)
    app.register_blueprint(second_query_native)
    app.register_blueprint(second_query_orm)
    app.register_blueprint(complaint)
    app.register_blueprint(driver)
    app.register_blueprint(order)
    app.register_blueprint(customer)
    app.register_blueprint(customer_orders)
    app.register_blueprint(edit_card)
