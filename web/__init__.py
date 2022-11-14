#!/usr/bin/env python
# encoding: utf-8

# DO WPROWADZANIA ZMIAN W KONTENERZE:
# docker-compose -d --build
# docker-compose up
import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.getenv("CONFIG_PATH", "app.config.Config"))
db = SQLAlchemy(app)
migrate = Migrate(app, db)
