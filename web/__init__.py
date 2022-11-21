#!/usr/bin/env python
# encoding: utf-8

# DO WPROWADZANIA ZMIAN W KONTENERZE:
# docker-compose -d --build
# docker-compose up
import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config.from_object(os.getenv("CONFIG_PATH", "app.config.Config"))
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db_psycopg = psycopg2.connect(
    dbname=app.config.get("DB_NAME"),
    user=app.config.get("DB_USER"),
    password=app.config.get("DB_PASSWORD"),
    host=app.config.get("DB_HOST"),
    port=app.config.get("DB_PORT")
)
