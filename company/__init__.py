# Company/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config["SECRET_KEY"] = "mysecret"
########################################################
from company.core.views import core #blueprint
from company.Count_visitor.views import views # blueprint
from company.error_pages.handlers import error_pages # blueprint
from company.users.views import users
app.register_blueprint(core)
app.register_blueprint(views)
app.register_blueprint(error_pages)
app.register_blueprint(users)
#######################################################
### Database Setup##
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:asengame@db:5432/postgres_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app,db)
#######################################################
### Login Configs ###
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"
