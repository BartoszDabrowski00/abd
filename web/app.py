from web import db, app
from web.models.models import *
from web.routes.register_rotues import register_routes


def reset_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


# def create_entities():
#     example_user = User(email='example@example.com')
#     test_user = User(email='test@test.com')
#     db.session.add(example_user)
#     db.session.add(test_user)
#     db.session.commit()
#     db.session.refresh(example_user)
#     samsung_phone = Phone(brand_name='Samsung', year=2019, owner_id=example_user.id)
#     iphone = Phone(brand_name='Apple', year=2021, owner_id=test_user.id)
#     xiaomi = Phone(brand_name='Xiaomi', year=2022, owner_id=test_user.id)
#     db.session.add(samsung_phone)
#     db.session.add(xiaomi)
#     db.session.add(iphone)
#     db.session.commit()


def init_db():
    reset_db()
    # create_entities()


if __name__ == "__main__":
    with app.app_context():
        init_db()
        register_routes(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
