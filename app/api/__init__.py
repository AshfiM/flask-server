from flask import Blueprint

dataSets_bp = Blueprint("datatsets", __name__)
from . import datasets

users_bp = Blueprint("users", __name__)
from . import users
