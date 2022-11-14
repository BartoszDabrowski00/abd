from dataclasses import dataclass

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from web import db


@dataclass
class Order(db.Model):
    __tablename__ = "orders"

    order_id: int = db.Column(db.Integer, primary_key=True)
    end_location: str = db.Column(db.String(512))
    end_time: str = db.Column(db.String(512))
    is_canceled: bool = db.Column(db.Boolean())
    is_completed: bool = db.Column(db.Boolean())
    number_of_passengers: int = db.Column(db.Integer)
    order_start_time: str = db.Column(db.String(128))
    order_time: str = db.Column(db.String(128))
    payment_method: int = db.Column(db.String(64))
    price: float = db.Column(db.Float)
    rating: int = db.Column(db.Integer)
    start_location: str = db.Column(db.String(512))
    trunk_volume: float = db.Column(db.Float)
    driver_login: str = db.Column(db.String, ForeignKey("drivers.login"))
    customer_login: str = db.Column(db.String, ForeignKey("customers.login"))

    complaint = relationship("Complaint", backref="order", lazy="select")
    customer = relationship("Customer", backref="orders", lazy="joined")
    driver = relationship("Driver", backref="orders", lazy="joined")


@dataclass
class Customer(db.Model):
    __tablename__ = "customers"

    login: str = db.Column(db.String(128), primary_key=True)
    name_and_surname: str = db.Column(db.String(256))
    password_hash: str = db.Column(db.String(128))
    phone_number: str = db.Column(db.String(20))
    is_automatic_payment_enabled: bool = db.Column(db.Boolean())
    card_number: str = db.Column(db.String, ForeignKey("credit_cards.card_number"))

    credit_card = relationship("CreditCard", backref="customer", lazy="select")
    orders = relationship("Order", backref="customer", lazy="select")


@dataclass
class CreditCard(db.Model):
    __tablename__ = "credit_cards"

    card_number: str = db.Column(db.String(64), primary_key=True)
    cvc_code: str = db.Column(db.String(3))
    expiration_date: str = db.Column(db.String(64))

    customer = relationship("Customer", backref="credit_card", lazy="joined")


@dataclass
class Complaint(db.Model):
    __tablename__ = "complaints"

    complaint_id: int = db.Column(db.Integer, primary_key=True)
    date_of_submission: str = db.Column(db.String(64))
    description: str = db.Column(db.String(2048))
    status: str = db.Column(db.String(64))
    order_id: int = db.Column(db.Integer, ForeignKey("orders.order_id"))

    order = relationship("Order", backref="complaint", lazy="joined")


@dataclass
class Car(db.Model):
    __tablename__ = "cars"

    car_id: int = db.Column(db.Integer, primary_key=True)
    number_of_seats: int = db.Column(db.Integer)
    trunk_volume: float = db.Column(db.Float)

    driver = relationship("Driver", backref="car", lazy="joined")


@dataclass
class Driver(db.Model):
    __tablename__ = "drivers"

    login: str = db.Column(db.String(128), primary_key=True)
    name_and_surname: str = db.Column(db.String(256))
    password_hash: str = db.Column(db.String(128))
    phone_number: str = db.Column(db.String(20))
    is_currently_working: bool = db.Column(db.Boolean())
    rating: float = db.Column(db.Float())
    rating_count: int = db.Column(db.Integer)
    car_id: int = db.Column(db.Integer, ForeignKey("cars.car_id"))

    car = relationship("Car", backref="driver", lazy='joined')
    orders = relationship("Order", backref="driver", lazy="select")
