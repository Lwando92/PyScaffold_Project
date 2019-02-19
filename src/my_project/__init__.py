from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from pkg_resources import get_distribution, DistributionNotFound

application = Flask(__name__)
application.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# -*- coding: utf-8 -*-


try:
    # Change here if project is renamed and does not equal the package name
    dist_name = 'My_project'
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound

from my_project import routes