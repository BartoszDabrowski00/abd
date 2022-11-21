import os
from enum import Enum

basedir = os.path.abspath(os.path.dirname(__file__))


class RelationshipLoadingOptions(Enum):
    LAZY = "select"
    JOINED = "joined"
    SUBQUERY = "subquery"
    SELECTIN = "selectin"
    RAISE = "raise"
    NO_LOADING = "noload"


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True  # ustawienie na 'True' przydatne do zadań wykładowych i przy pracy nad sprawozdaniem 2
    RELATIONSHIP_LOADING = RelationshipLoadingOptions.LAZY.value
    SHOULD_REINIT_DB = False
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "flaskapp_dev")
    DB_USER = os.getenv("DB_USER", "flaskapp")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "flaskapp")

