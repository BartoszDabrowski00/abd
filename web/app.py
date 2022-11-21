from web import db, app
from web.routes.register_rotues import register_routes
from web.utils.data_generator.generator import generate_db


def reset_db() -> None:
    db.drop_all()
    db.create_all()
    db.session.commit()


def create_entities() -> None:
    orders, complaints, drivers, cars, customers, credit_cards = generate_db()
    session = db.session
    session.add_all(drivers)
    session.add_all(cars)
    session.add_all(credit_cards)
    session.add_all(customers)
    session.add_all(orders)
    session.add_all(complaints)
    session.commit()


def init_db() -> None:
    if app.config.get("SHOULD_REINIT_DB"):
        reset_db()
        create_entities()


if __name__ == "__main__":
    with app.app_context():
        init_db()
        register_routes(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
