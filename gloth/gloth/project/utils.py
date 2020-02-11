import os
from .models import *

### Renvoie la liste de toutes les maladies
def pathologyChoices():

    temp = Pathology.query.with_entities(Pathology.id, Pathology.name, Pathology.other_name, Pathology.description).all()
    other_name_temp = []

    for x in temp:
        if x[2]:
            array = x[2].split(",")

            for i in range(len(array)):
                if array[i] is not None:
                    other_name_temp.append((x[0], array[i].strip()))

    choices = [(x[0], x[1]) for x in temp] + other_name_temp

    i = 0
    l = len(choices)
    while (i < l and choices[i]):
        if choices[i][1] == '':
            del choices[i]
            l -= 1
        else:
            i += 1

    return choices

#renvoie la liste de tous les users
def userChoices():

    temp = User.query.with_entities(User.id, User.forename).all()
    choices = [(x[0], x[1]) for x in temp]
    return choices


# Renvoi la deescription de la pathologie
def getPathologyDescription(pathology) :
    pathox = Pathology.query.filter_by(id=pathology).with_entities(Pathology.description).first()
    return pathox


# Renvoi l
def getPathologyname(pathology):#name
    pathox = Pathology.query.filter_by(id=pathology).with_entities(Pathology.name).first()
    return pathox


# Renvoi l
def getPathologyIcd10(pathology):#icd10
    pathox = Pathology.query.filter_by(id=pathology).with_entities(Pathology.icd_10).first()
    return pathox

#
"""

    pathox=str(pathox).replace('(','')
    pathox=pathox.replace(')','')
    pathox=pathox.replace(',','')
    pathox=pathox.replace(']','')
    pathox=pathox.replace('[','')
"""


# Renvoi l
def getTreatmentClassName(icd_10x):#pathology name
    pathox = TreatmentClass.query.filter_by(icd_10=icd_10x).with_entities(TreatmentClass.pathology_name).all()
    pathox=str(pathox).replace('(','')
    pathox=pathox.replace(')','')
    pathox=pathox.replace(',','')
    pathox=pathox.replace(']','')
    pathox=pathox.replace('[','')
    return pathox


# Renvoi l
def getTreatmentClassx(icd_10x):#pathology name
    pathox = TreatmentClass.query.filter_by(icd_10=icd_10x).with_entities(TreatmentClass.class_id).all()
    return pathox


# Renvoi l
def getTreatmentClassId(icd_10x):#pathology name
    pathox = TreatmentClass.query.filter_by(icd_10=icd_10x).with_entities(TreatmentClass.class_id).all()
    pathox=str(pathox).replace('(','')
    pathox=pathox.replace(')','')
    pathox=pathox.replace(',','')
    pathox=pathox.replace(']','')
    pathox=pathox.replace('[','')
    return pathox


# Renvoi le nom de la classe
def getClassClassName(classId) :
    className = ClassClass.query.filter_by(id=classId).with_entities(ClassClass.name).first()
    return className


# Renvoi le nom de la molécule
def getTreatmentMoleculeName(icd_10x):
    moleculeName = TreatmentMolecule.query.filter_by(icd_10=icd_10x).with_entities(TreatmentMolecule.pathology_name).all()
    return moleculeName


# Renvoi les IDs des molécules du traitement
def getTreatmentMoleculeId(icd_10x):
    moleculeId = TreatmentMolecule.query.filter_by(icd_10=icd_10x).with_entities(TreatmentMolecule.molecule_id).all()
    return moleculeId


# Renvoi les noms des médicaments
def getTreatmentCisName(icd_10x):
    cisName = TreatmentCis.query.filter_by(icd_10=icd_10x).with_entities(TreatmentCis.pathology_name).all()
    return cisName


# Renvoi les noms des médicaments
def getMedication(molecule_idx):
    mediName = Medication.query.filter_by(molecule_id=molecule_idx).with_entities(Medication.name).all()
    return mediName


# Renvoi la pathologie
def getPathology(pathoId):
    patho = Pathology.query.filter_by(id=pathoId).with_entities(Pathology.name).first()
    return patho


# Renvoi les IDs des
def getLinkedPatho(pathoId):
    icd_10 = getPathologyIcd10(pathoId)
    icdClass = getTreatmentClassId(icd_10)
    icdClassx = icdClass.split(' ')
    strIds = []
    for x in range(0, len(icdClassx)-1):
        strIds += getClassClassName(icdClassx[x])
    return str(strIds)

