from flask import Flask
from config import config
import os

from .extensions import jwt, db
from .auth