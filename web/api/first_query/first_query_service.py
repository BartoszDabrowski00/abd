import time

import psycopg2
from sqlalchemy import and_
from sqlalchemy.orm import joinedload, lazyload

from web import db, app
from web.models.models import Complaint, Order, Customer


def demonstrate_first_query_orm(user_login, order_start_time, complaint_time, status_to_update):
    start_time = time.time()
    session = db.session
    complaint = session.query(Complaint).join(Order).join(Customer).options(
        joinedload(Complaint.order).options(joinedload(Order.driver), lazyload(Order.customer))).filter(
        and_(
            Customer.login == user_login,
            Order.order_start_time == order_start_time,
            Complaint.date_of_submission == complaint_time)
    ).first()

    complaint.status = status_to_update
    driver = complaint.order.driver
    driver.rating -= 2
    driver.rating_count += 1
    session.commit()
    end_time = time.time()
    print(f"Operation took {end_time - start_time}")


def demonstrate_first_query_native(user_login, order_start_time, complaint_time, status_to_update):
    start_time = time.time()
    with psycopg2.connect(dbname=app.config.get("DB_NAME"), user=app.config.get("DB_USER"),
                          password=app.config.get("DB_PASSWORD"), host=app.config.get("DB_HOST"),
                          port=app.config.get("DB_PORT")) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"""
            UPDATE complaints
                SET 
                    status = '{status_to_update}'
                FROM orders as ord
                    JOIN customers as cust ON ord.customer_login = cust.login
                    JOIN complaints as comp ON ord.order_id = comp.order_id
                WHERE
                    comp.date_of_submission = '{complaint_time}' AND
                    ord.order_start_time = '{order_start_time}' AND
                    cust.login = '{user_login}';
                
            UPDATE drivers
                SET
                    rating = dri.rating - 2,
                    rating_count = dri.rating_count + 1
                FROM orders as ord
                    JOIN customers as cust ON ord.customer_login = cust.login
                    JOIN complaints as comp ON ord.order_id = comp.order_id
                    JOIN drivers as dri ON ord.driver_login = dri.login
                WHERE
                    comp.date_of_submission = '{complaint_time}' AND
                    ord.order_start_time = '{order_start_time}' AND
                    cust.login = '{user_login}';""")
    end_time = time.time()
    print(f"Operation took {end_time - start_time}")
