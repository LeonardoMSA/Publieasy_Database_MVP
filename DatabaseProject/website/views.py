from flask import render_template, url_for, redirect, request, Blueprint, flash
from DatabaseProject.models import db
from DatabaseProject.models import Motorista, Anuncio, Cliente, Contrato, Count, QRCode
from DatabaseProject.forms import AddQrForm
import smtplib
import os
import qrcode
import shutil

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

# Fazer login de adm aqui p/ poder ver estatisticas/erp
@website.route('/estatistica')
def statistics():

    return render_template('statistics.html')

@website.route('/contato')
def contact():

    return render_template('contact.html')

@website.route('/addQR', methods=["GET", "POST"])
def addQR():

    form = AddQrForm()

    if form.validate_on_submit():
        apelido = form.apelido.data
        nomeArquivo = form.nomeArquivo.data
        link = form.link.data
        anunciante = form.anunciante.data

        qr =qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_L,
                  box_size=40,
                  border=1)

        qr.add_data(f"www.publieasy.com/qr_redirect/{apelido}")
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        save_dir = "DatabaseProject/static/uploads"

        os.makedirs(save_dir, exist_ok=True)

        destination_path = os.path.join(save_dir, nomeArquivo)
        img.save(destination_path)

        image = url_for('static', filename=f'uploads/{nomeArquivo}')

        qr1 = QRCode(acessos_total = 0, acesso_unico = 0,imagem_qr = image, apelido = apelido,
                      nome_arquivo = nomeArquivo, link = link, anunciante = anunciante)

        db.session.add(qr1)
        db.session.commit()

        qr2 = QRCode.query.filter_by(apelido = apelido).first()

        return redirect(url_for('website.index'))

    return render_template("addQrCode.html", form=form)


@website.route('/qr_redirect/<nick>')
def qr_redirect(nick):

    qr = QRCode.query.filter_by(apelido = nick).first()

    qr.acessos_total += 1
    db.session.commit()

    return redirect(f"{qr.link}", code=302)

