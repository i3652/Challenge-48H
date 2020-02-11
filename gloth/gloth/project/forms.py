from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, BooleanField, TextAreaField, StringField,SelectMultipleField
from wtforms import PasswordField, DecimalField
from wtforms_components import IntegerField
from wtforms.fields.html5 import EmailField, DateTimeLocalField
from wtforms import validators
from .utils import *

class PatientForm(FlaskForm):
    pathology = SelectField("Pathologie", validators = [validators.InputRequired()], id = "pathology", choices = pathologyChoices())
    user = SelectField("Docteur", validators = [validators.InputRequired()], id = "user", choices = userChoices())
    submit = SubmitField("Valider")

class MedicForm(FlaskForm):
    submit = SubmitField("Valider")

class linkedForm(FlaskForm):
    choicelinked = SelectField("choicelinked", validators=[validators.InputRequired()], id="choicelinked",choices=[] )
    classx = SelectField("classx", validators=[validators.InputRequired()], id="classx",choices=[] )
    Molecule = SelectField("Molecule", validators=[validators.InputRequired()], id="Molecule",choices=[] )
    medicament = SelectField("medicament", validators=[validators.InputRequired()], id="medicament",choices=[] )
    submit = SubmitField("Valider")



"""
chaque choix on doit leur attribuer une classe precise pour la recuperer en fonction de son parent 
class>Molecule>medicament
puis affichage des selects en javascript 
ou 
si plus de temps
Create dynamic select field flask javacript
https://www.youtube.com/watch?v=I2dJuNwlIH0
"""