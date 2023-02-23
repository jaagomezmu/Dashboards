import locale

locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

import os

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

# Create two constant. They direct to the app root folder and logo upload folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static', 'wordmaps')


# Create app
app = Flask(__name__)
bootstrap = Bootstrap5(app)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class FiltroForm(FlaskForm):
    pais = SelectMultipleField('PAIS',
                               choices=[('Argentina', 'Argentina'),
                                        ('Brasil', 'Brasil'),
                                        ('Chile', 'Chile'),
                                        ('Colombia', 'Colombia'),
                                        ('Ecuador', 'Ecuador'),
                                        ('Guatemala', 'Guatemala'),
                                        ('México', 'México'),
                                        ('Panamá', 'Panamá'), 
                                        ('Perú', 'Perú')],
                               validators=[DataRequired()])
    sexo = SelectMultipleField('SEXO',
                               choices=[('Hombre', 'Hombre'),
                                        ('Mujer', 'Mujer')],
                               validators=[DataRequired()])
    tipo_contratacion = SelectMultipleField('TIPO CONTRATACION',
                               choices=[('Directo', 'Directo'),
                                        ('Outsourcing', 'Outsourcing')],
                               validators=[DataRequired()])
    submit = SubmitField('APLICAR')


###
##Configuration dictionary
###
app.config['DEBUG'] = True
# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'flatly'

########################
### Register blueprints
########################
