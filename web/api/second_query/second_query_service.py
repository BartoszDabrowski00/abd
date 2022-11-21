import time

import psycopg2
from sqlalchemy import and_

from web import app, db
from web.models.models import Customer, Order, Driver, Complaint, Car


def demonstrate_second_query_orm(num_of_seats: int, start_date: str, end_date: str) -> [Customer]:
    start_time = time.time()
    session = db.session
    results = Customer.query.with_entities(Customer.login, Customer.name_and_surname, Customer.phone_number) \
        .join(Order).join(Complaint).join(Driver).join(Car) \
        .filter(
        and_(
            Complaint.status == "completed",
            Car.number_of_seats == num_of_seats,
            Order.order_start_time <= end_date,
            Order.order_start_time >= start_date
        )
    ).all()

    session.commit()
    end_time = time.time()
    print(f"Operation took {end_time - start_time}")
    return [dict(elem) for elem in results]


def demonstrate_second_query_native(num_of_seats: int, start_date: str, end_date: str) -> [Customer]:
    start_time = time.time()
    with psycopg2.connect(dbname=app.config.get("DB_NAME"), user=app.config.get("DB_USER"),
                          password=app.config.get("DB_PASSWORD"), host=app.config.get("DB_HOST"),
                          port=app.config.get("DB_PORT")) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"""
                SELECT cust.login, cust.name_and_surname, cust.phone_number
                FROM customers cust 
                    JOIN orders ord on ord.customer_login = cust.login
                    JOIN complaints comp on comp.order_id = ord.order_id
                    JOIN drivers dri on dri.login = ord.driver_login
                    JOIN cars cr on cr.car_id = dri.car_id
                WHERE
                    comp.status = 'completed'
                    AND cr.number_of_seats = {num_of_seats}
                    AND ord.order_start_time <= '{end_date}'
                    AND ord.order_start_time >= '{start_date}';
	        """)
            results = cursor.fetchall()
    end_time = time.time()
    print(f"Operation took {end_time - start_time}")
    return [{"login": elem[0], "name_and_surname": elem[1], "phone_number": elem[2]} for elem in results]
