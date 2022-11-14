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
    SQLALCHEMY_ECHO = False  # ustawienie na 'True' przydatne do zadań wykładowych i przy pracy nad sprawozdaniem 2
    RELATIONSHIP_LOADING = RelationshipLoadingOptions.LAZY.value
