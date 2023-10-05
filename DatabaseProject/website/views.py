from flask import render_template, url_for, redirect, request, Blueprint, flash
from DatabaseProject import db
from DatabaseProject.models import Driver, Anuncio

website = Blueprint('website', __name__)

@website.route('/')
def index():

    return render_template('index.html')

@website.route('/servicos')
def services():

    return render_template('services.html')

@website.route('/estatistica')
def statistics():

    return render_template('statistics.html')

@website.route('/contato')
def contact():

    return render_template('contact.html')
