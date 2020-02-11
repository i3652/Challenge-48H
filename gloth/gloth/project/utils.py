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


#PATHOLOGY3333333333333333333333333333333333333333333333

def getPathologydescription(pathology):#description
    pathox = Pathology.query.filter_by(id=pathology).with_entities(Pathology.description).first()
    pathox = cleanchar(pathox)
    return pathox

def getPathologyname(pathology):#name
    pathox = Pathology.query.filter_by(id=pathology).with_entities(Pathology.name).first()
    pathox = cleanchar(pathox)
    return pathox

def getPathologyIcd10(pathology):#icd10
    pathox = Pathology.query.filter_by(id=pathology).with_entities(Pathology.icd_10).first()
    pathox = cleanchar(pathox)
    return pathox

#TREATMENTCLASS3333333333333333333333333333333333333333333333

def getTreatmentClassName(icd_10x):#pathology name
    pathox = TreatmentClass.query.filter_by(icd_10=icd_10x).with_entities(TreatmentClass.pathology_name).all()
    pathox = cleanchar(pathox)
    return pathox

def getTreatmentClassx(icd_10x):#pathology name
    pathox = TreatmentClass.query.filter_by(icd_10=icd_10x).with_entities(TreatmentClass.class_id).all()
    return pathox

def getTreatmentClassid(icd_10x):#pathology name
    pathox = TreatmentClass.query.filter_by(icd_10=icd_10x).with_entities(TreatmentClass.class_id).all()
    pathox=str(pathox).replace('(','')
    pathox=pathox.replace(')','')
    pathox=pathox.replace(',','')
    pathox=pathox.replace(']','')
    pathox=pathox.replace('[','')
    return pathox

def getClassClassName(icd_10x):#pathology name
    pathox = ClassClass.query.filter_by(icd_10=icd_10x).with_entities(ClassClass.name).first()
    pathox = cleanchar(pathox)
    return pathox
#TREATMENTMOLECULE3333333333333333333333333333333333333333333333

def getTreatmentMoleculeName(icd_10x):#pathology name
    pathox = TreatmentMolecule.query.filter_by(icd_10=icd_10x).with_entities(TreatmentMolecule.pathology_name).all()
    pathox = cleanchar(pathox)
    return pathox

def getTreatmentMoleculeid(icd_10x):#pathology name
    pathox = TreatmentMolecule.query.filter_by(icd_10=icd_10x).with_entities(TreatmentMolecule.molecule_id).all()
    pathox = cleanchar(pathox)
    return pathox
#TREATMENTMOLECULE3333333333333333333333333333333333333333333333
def getTreatmentCisName(icd_10x):#pathology name
    pathox = TreatmentCis.query.filter_by(icd_10=icd_10x).with_entities(TreatmentCis.pathology_name).all()
    pathox = cleanchar(pathox)
    return pathox
#MEDICATIONE3333333333333333333333333333333333333333333333
def getmedication(molecule_idx):#pathology name
    pathox = Medication.query.filter_by(molecule_id=molecule_idx).with_entities(Medication.name).all()
    pathox = cleanchar(pathox)
    return pathox



def getPathology(pathology):
    pathox = Pathology.query.filter_by(id=pathology).with_entities(Pathology.name).first()
    pathox = cleanchar(pathox)
    return pathox


def cleanchar(strx):

    return strx






def getLinkedPatho(patho_id):
    icd_10 = getPathologyIcd10(patho_id)
    icdclass = getTreatmentClassid(icd_10)
    pikachuclass= []
    idclass=icdclass.split(' ')
    for i in range(len(icdclass)):
        pikachuclass[i]=getClassClassName(idclass[i])
    return str(pikachuclass)

