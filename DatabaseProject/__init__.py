import json
import os
from datetime import datetime

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import (Flask, abort, flash, redirect, render_template, request,
                   url_for)
from flask_bootstrap import Bootstrap
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import check_password_hash, generate_password_hash

from .models import db, Cliente, Contrato, Anuncio, Motorista

load_dotenv()

app = Flask(__name__)

#########################
####### DB SETUP ########
#########################

app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DB_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
db.init_app(app)

with app.app_context():
	db.create_all()

from DatabaseProject.website.views import website
from DatabaseProject.error_pages.handlers import error_pages

app.register_blueprint(website)
app.register_blueprint(error_pages)

