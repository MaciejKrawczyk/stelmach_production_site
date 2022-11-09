from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session.__init__ import Session
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO


class ConfigClass(object):
    SECRET_KEY = 'thisisasecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy warning
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"


app = Flask(__name__)
app.config.from_object(__name__ + '.ConfigClass')
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
Session(app)
socket = SocketIO(app)

from pipe import routes
