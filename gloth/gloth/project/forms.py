from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, BooleanField, TextAreaField, StringField,SelectMultipleField
from wtforms import PasswordField, DecimalField
from wtforms_components import IntegerField
from wtforms.fields.html5 import EmailField, DateTimeLocalField
from wtforms import validators
from .utils import *

class PatientForm(FlaskForm):
    pathology = SelectMultipleField("Pathologie", validators = [validators.InputRequired()], id = "pathology", choices = pathologyChoices())
    user = SelectField("Docteur", validators = [validators.InputRequired()], id = "user", choices = userChoices())
    submit = SubmitField("Valider")

class MedicForm(FlaskForm):
    submit = SubmitField("Valider")

class linkedForm(FlaskForm):
    choicelinked = SelectMultipleField("linkedchoice", validators = [validators.InputRequired()], id = "choicelinked", )
    submit = SubmitField("Valider")
