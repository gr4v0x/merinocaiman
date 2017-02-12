from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

import xml.etree.ElementTree as ET

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('X', 'Non-Binary'),
)

COUNTRIES = []
country_tree = ET.parse('/etc/countries.xml')
country_root = country_tree.getroot()
for child in country_root:
    COUNTRIES.append((child.get('alpha-2'), child.get('name')))

PERSON_TYPE = (
    ('witness', 'Witness'),
    ('informant', 'Informant'),
    ('suspect', 'Suspect'),
    ('enabler', 'Enabler'),
)

# Create your models here.
class Case(models.Model):
    referenceOne = models.CharField(max_length=25)
    referenceTwo = models.CharField(max_length=25)
    caseNameOne = models.CharField(max_length=256)
    caseNameTwo = models.CharField(max_length=256)
    user = models.ForeignKey(User)
    caseRefKey = models.CharField(max_length=45, primary_key=True)


class MainIden(models.Model):
    lastName = models.CharField(max_length=256)
    firstName = models.CharField(max_length=256)
    otherName = models.CharField(max_length=512, null=True)
    gender = models.CharField(max_length=12, choices=GENDER, null=True)
    dateOfBirth = models.DateField(null=True)
    cityOfBirth = models.CharField(max_length=256)
    countryOfBirth = models.CharField(max_length=256, choices=COUNTRIES)
    idenType = models.CharField(max_length=64, choices=PERSON_TYPE, null=True)
    dateTimeAdded = models.DateTimeField(auto_now_add=True)
    mainIdenKey = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        l_name = self.lastName
        f_name = self.firstName

        return l_name.upper() + ", " + f_name


class AliasIden(models.Model):
    lastName = models.CharField(max_length=256)
    firstName = models.CharField(max_length=256)
    otherName = models.CharField(max_length=512)
    dateOfBirth = models.DateField(null=True)
    cityOfBirth = models.CharField(max_length=256)
    countryOfBirth = models.CharField(max_length=256)
    dateTimeAdded = models.DateTimeField(auto_now_add=True)
    aliasIdenKey = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        l_name = self.lastName
        f_name = self.firstName

        return l_name.upper() + ", " + f_name


class AliasAssoc(models.Model):
    main = models.ForeignKey('MainIden', on_delete=models.CASCADE)
    alias = models.ForeignKey('AliasIden', on_delete=models.CASCADE)
    attribDate = models.DateField(null=True)
    sourceDocument = models.ForeignKey('Document', on_delete=models.CASCADE)
    aliasAssocKey = models.CharField(max_length=45, primary_key=True)


class Document(models.Model):
    number = models.CharField(max_length=5)
    docType = models.CharField(max_length=128)


class Address(models.Model):
    optionalPrefix = models.CharField(max_length=255)
    streetNumber = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    addressLineOne = models.CharField(max_length=255)
    addressLineTwo = models.CharField(max_length=255)
    addressLineThree = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    dateTimeAdded = models.DateTimeField(auto_now_add=True)
    addresKey = models.CharField(max_length=45, primary_key=True)


class Task(models.Model):
    task = models.CharField(max_length=2048)
    priority = models.CharField(max_length=25)
    dueDate = models.DateField()
    taskKey = models.CharField(max_length=45, primary_key=True)


class NoteBook(models.Model):
    note = models.CharField(max_length=20000)
    noteDate = models.DateField()
    noteTime = models.TimeField()
    subject = models.CharField(max_length=255)
    dateTimeAdded = models.DateTimeField(auto_now_add=True)
    noteKey = models.CharField(max_length=45, primary_key=True)
