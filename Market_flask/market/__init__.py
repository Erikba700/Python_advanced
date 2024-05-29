from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '0336fae0040444e76651d0c9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Addcry700@localhost/market'
bycrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = 'info'
db = SQLAlchemy(app)

from . import routes
