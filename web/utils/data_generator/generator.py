import configparser
import datetime
import os
import random
import string

from faker import Faker

from web.models.models import Car, Driver, CreditCard, Customer, Order, Complaint

orders = []
customers = []
credit_cards = []
complaints = []
cars = []
drivers = []

faker = Faker()
letters = string.ascii_letters
numbers = string.digits
config = configparser.ConfigParser()
config.read(os.getenv("GENERATOR_CONFIG_PATH", "generator_config.cfg"))


def get_random_string(size: int) -> str:
    return ''.join(random.choice(letters) for _ in range(size))


def get_random_number(size: int) -> str:
    return ''.join(random.choice(numbers) for _ in range(size))


def generate_drivers_and_cars() -> None:
    for i in range(config.getint("generator", "drivers")):
        car = Car(number_of_seats=random.randint(4, 7), trunk_volume=random.uniform(20, 60))
        driver = Driver()
        driver.login=get_random_string(10)
        driver.name_and_surname=get_random_string(40)
        driver.password_hash=get_random_string(20)
        driver.phone_number=get_random_number(9)
        driver.is_currently_working=bool(random.randint(0, 1))
        driver.rating=random.uniform(0, 5)
        driver.rating_count=random.randint(0, 100)
        driver.car = car
        cars.append(car)
        drivers.append(driver)


def generate_customers_and_credit_cards() -> None:
    for i in range(config.getint("generator", "customers")):
        credit_card = CreditCard(
            card_number=get_random_number(20),
            cvc_code=get_random_number(3),
            expiration_date=faker.date_between(start_date=datetime.date(year=2000, month=1, day=1), end_date='+3y')
        )
        customer = Customer()
        customer.login=get_random_string(10)
        customer.name_and_surname=get_random_string(40)
        customer.password_hash=get_random_string(20)
        customer.phone_number=get_random_number(9)
        customer.is_automatic_payment_enabled=bool(random.randint(0, 1))
        credit_card.customer.append(customer)
        credit_cards.append(credit_card)
        customers.append(customer)


def generate_orders_and_complaints() -> None:
    for i in range(config.getint("generator", "orders")):
        order = Order()
        order.end_location=get_random_string(40)
        order.end_time=faker.iso8601()
        order.is_canceled=bool(random.randint(0, 1))
        order.is_completed=bool(random.randint(0, 1))
        order.number_of_passengers=random.randint(1, 4)
        order.order_start_time=faker.iso8601()
        order.order_time=faker.iso8601()
        order.payment_method=get_random_string(10)
        order.price=random.uniform(10, 100)
        order.rating=random.uniform(0, 5)
        order.start_location=get_random_string(40)
        order.trunk_volume=random.uniform(20, 60)
        order.customer = random.choice(customers)
        order.driver = random.choice(drivers)
        if i % 15 == 0:
            complaint = Complaint()
            complaint.date_of_submission=faker.iso8601()
            complaint.description=get_random_string(100)
            complaint.status=random.choice(["completed", "declined"])
            complaint.order = order
            complaints.append(complaint)
        orders.append(order)


def generate_db() -> ([Order], [Complaint], [Driver], [Car], [Customer], [CreditCard]):
    generate_drivers_and_cars()
    generate_customers_and_credit_cards()
    generate_orders_and_complaints()
    return orders, complaints, drivers, cars, customers, credit_cards
