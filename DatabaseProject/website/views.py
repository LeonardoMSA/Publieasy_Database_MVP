from flask import render_template, url_for, redirect, request, Blueprint, flash
from DatabaseProject.models import db
from DatabaseProject.models import Motorista, Anuncio, Cliente, Contrato, Count
import smtplib
import os

website = Blueprint('website', __name__)

@website.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        email = request.form.get('email')
        celular = request.form.get('celular')
        nomeEmpresa = request.form.get('nome-empresa')

        msg = f"Subject: Nova solicitação de anúncio\n\nNome da empresa: {nomeEmpresa}\nEmail: {email}\nCelular: {celular}"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("leomenezes12345@gmail.com", "awhq soye muli ddqy ")
        msg_encoded = msg.encode('utf-8')
        server.sendmail("leomenezes12345@gmail.com", "comercialpublieasy@gmail.com", msg_encoded)



    client = Cliente.query.filter_by(setor='sexual').first()

    return render_template('index.html', client=client)

@website.route('/endomarketing')
def services():

    count = Count.query.get(1)
    if count is None:
        count = Count(1)
        db.session.add(count)
        db.session.commit()

    

    print(f"{count.accessCount}")
    count.accessCount += 1
    count1 = count.accessCount

    db.session.commit()

    return render_template('endomarketing.html', count = count1)

@website.route('/estatistica')
def statistics():

    return render_template('statistics.html')

@website.route('/contato')
def contact():

    return render_template('contact.html')
