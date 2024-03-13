from flask_wtf import FlaskForm
from wtforms import FileField, FloatField, BooleanField,StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class AddQrForm(FlaskForm):
    apelido = StringField("Apelido qr: (ex: carlos.png)", validators=[DataRequired(), Length(max=150)])
    link = StringField("Link para direcionar:", validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Post')
