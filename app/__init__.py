from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "key_secrtr"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

from .admin import *
from .models import *
from .views import *
