from flask import render_template, url_for, redirect, request, Blueprint, flash
from DatabaseProject import db
from DatabaseProject.models import Driver, Anuncio, Count

website = Blueprint('website', __name__)

@website.route('/')
def index():

    

    return render_template('index.html')

@website.route('/servicos')
def services():

    count = Count.query.get(0)
    if count is None:
        count = Count(1)
        db.session.add(count)
        db.session.commit()

    print(f"{count.accessCount}")
    count.accessCount += 1
    count1 = count.accessCount

    db.session.commit()

    return render_template('services.html', count = count1)

@website.route('/estatistica')
def statistics():

    return render_template('statistics.html')

@website.route('/contato')
def contact():

    return render_template('contact.html')
