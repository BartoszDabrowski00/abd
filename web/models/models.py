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
    payment_method: str = db.Column(db.String(64))
    price: float = db.Column(db.Float)
    rating: int = db.Column(db.Integer)
    start_location: str = db.Column(db.String(512))
    trunk_volume: float = db.Column(db.Float)
    driver_login: str = db.Column(db.String, ForeignKey("drivers.login"))
    customer_login: str = db.Column(db.String, ForeignKey("customers.login"))

    complaint = relationship("Complaint", back_populates="order", lazy="joined")
    customer = relationship("Customer", back_populates="orders", lazy="select")
    driver = relationship("Driver", back_populates="orders", lazy="select")


@dataclass
class User:
    login: str = db.Column(db.String(128), primary_key=True)
    name_and_surname: str = db.Column(db.String(256))
    password_hash: str = db.Column(db.String(128))
    phone_number: str = db.Column(db.String(20))


@dataclass
class Customer(User, db.Model):
    __tablename__ = "customers"

    is_automatic_payment_enabled: bool = db.Column(db.Boolean())
    card_number: str = db.Column(db.String, ForeignKey("credit_cards.card_number"))

    orders = relationship("Order", back_populates="customer", lazy="joined")
    credit_card = relationship("CreditCard", back_populates="customer", lazy="joined")


@dataclass
class CreditCard(db.Model):
    __tablename__ = "credit_cards"

    card_number: str = db.Column(db.String(20), primary_key=True)
    cvc_code: str = db.Column(db.String(3))
    expiration_date: str = db.Column(db.String(64))

    customer = relationship("Customer", back_populates="credit_card", lazy="select")


@dataclass
class Complaint(db.Model):
    __tablename__ = "complaints"

    complaint_id: int = db.Column(db.Integer, primary_key=True)
    date_of_submission: str = db.Column(db.String(64))
    description: str = db.Column(db.String(2048))
    status: str = db.Column(db.String(64))
    order_id: int = db.Column(db.Integer, ForeignKey("orders.order_id"))

    order = relationship("Order", back_populates="complaint", lazy="select")


@dataclass
class Car(db.Model):
    __tablename__ = "cars"

    car_id: int = db.Column(db.Integer, primary_key=True)
    number_of_seats: int = db.Column(db.Integer)
    trunk_volume: float = db.Column(db.Float)

    driver = relationship("Driver", back_populates="car", lazy="joined")


@dataclass
class Driver(User, db.Model):
    __tablename__ = "drivers"

    is_currently_working: bool = db.Column(db.Boolean())
    rating: float = db.Column(db.Float())
    rating_count: int = db.Column(db.Integer)
    car_id: int = db.Column(db.Integer, ForeignKey("cars.car_id"))

    car = relationship("Car", back_populates="driver", lazy='joined')
    orders = relationship("Order", back_populates="driver", lazy="joined")

