import os
from werkzeug import secure_filename
from flask import Flask, request, redirect, url_for, render_template, flash
app = Flask(__name__)
app.config.from_object("project.config.Config")

from .forms import PatientForm, MedicForm,linkedForm
from .utils import *

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = PatientForm()

    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required.")
            return render_template("index.html", title="Gloth", subtitle="test", patient_form=form, name="Ynov")
        else:
            data = request.args.get(form)
            return redirect(url_for('medic'), data=data)

    return render_template("index.html", title="Gloth", subtitle="subtitle", patient_form=form, name="Ynov")


@app.route('/medic', methods=["GET","POST"])
def medic():
  
    form = MedicForm(request.form)
    patho_id = (request.form.get("pathology"))
    user_id = (request.form.get("user"))
    icd_10 = getPathologyIcd10(patho_id)
    arrax = getTreatmentClassid(icd_10)
    classx=getLinkedPatho(patho_id)
    icdmolecule = getTreatmentMoleculeName(icd_10)
    icdclass = getTreatmentClassName(icd_10)
    icdcis = getTreatmentCisName(icd_10)
    pathologydescription = getPathologydescription(patho_id)
    
    return render_template("medic.html", name="Ynov",array=classx,patoinfox=pathologydescription,icdmolecule=icdmolecule)