from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SESSION_REDIS"] = "redis://:[password]@[host]:[port]"

from .admin import *
from .models import *
from .views import *
