import os

from flask import Flask



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "CrfQfSGOPD"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["FLASK_ADMIN_SWATCH"] = "flatly"

# DO NOT MOVE THIS IMPORTS TO TOP
from .admin import *
from .models import *
from .views import *
