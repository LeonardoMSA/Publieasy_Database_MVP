from flask_wtf import FlaskForm
from wtforms import FileField, FloatField, BooleanField,StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class AddQrForm(FlaskForm):
    apelido = StringField("Apelido qr: (ex: carlitos)", validators=[DataRequired(), Length(max=150)])
    nomeArquivo = StringField("Nome do arquivo: (ex: carlos.png)", validators=[DataRequired(), Length(max=150)])
    link = StringField("Link para direcionar: (ex: https://youtube.com)", validators=[DataRequired(), Length(max=200)])
    anunciante = StringField("Anunciante:", validators=[DataRequired(), Length(max=150)])
    submit = SubmitField('Post')
