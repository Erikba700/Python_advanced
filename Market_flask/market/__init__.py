import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

load_dotenv()  # loading personal and sensitive data to the current process

app = Flask(__name__)
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
app.config['SECRET_KEY'] = '0336fae0040444e76651d0c9'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_username}:{db_password}@localhost/market"
bycrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = 'info'
db = SQLAlchemy(app)

from . import routes
