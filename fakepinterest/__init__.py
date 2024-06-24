from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] =os.getenv("DATABASE_URL") #"sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "28d16c04"
app.config["UPLOAD_FODER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"


from fakepinterest import routes