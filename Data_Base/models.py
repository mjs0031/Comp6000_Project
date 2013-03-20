""" Python Package Imports """
from itertools import chain
from datetime import date, datetime, date, timedelta

""" Django Package Imports """
from django.db import models
from django.contrib.localflavor.us import models as us_models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

""" Internal Package Imports """
# Not Applicable

"""

 Data_Base/models.py
 Author(s)    : Matthew J Swann; Yong Kin; Bradon Atkins
 Version      : 1.0
 Last Revised : 2013-03-20
 Update By    : Matthew J Swann
 
 Code for the database tables and inherent functionality.

 """

SCHOOL_SET = (
    ('P', 'Primary'),
    ('S', 'Secondary'),
    ('C', 'Continuing Education'),
        ) 
 

class Business(models.Model):
    # Natural fields
    name                 = models.CharField(max_length=128)
    address_line_one     = models.CharField(max_length=128)
    address_line_two     = models.CharField(max_length=128, blank=True)
    city                 = models.CharField(max_length=32)
    state                = us_models.USStateField()
    zip_code             = models.CharField(max_length=10,
                               validators=[RegexValidator(r'^\d{5}(-\d{4})?$')])
    phone                = us_models.PhoneNumberField(blank=True)    
    notes                = models.TextField(blank=True)
    business_description = models.TextField(blank=True)
    
class School(models.Model):
    # Natural fields
    name                 = models.CharField(max_length=128)
    address_line_one     = models.CharField(max_length=128)
    address_line_two     = models.CharField(max_length=128, blank=True)
    city                 = models.CharField(max_length=32)
    state                = us_models.USStateField()
    zip_code             = models.CharField(max_length=10,
                               validators=[RegexValidator(r'^\d{5}(-\d{4})?$')])
    phone                = us_models.PhoneNumberField(blank=True)    
    notes                = models.TextField(blank=True)
    education_level      = models.CharField(max_length=1, choices=SCHOOL_SET, default='P')
    
class Person(models.Model):
    # Keyed Fields
    business = models.ForeignKey(Business, null=True)
    # Natural Fields
    first_name           = models.CharField(max_length=128)
    last_name            = models.CharField(max_length=128)
    address_line_one     = models.CharField(max_length=128)
    address_line_two     = models.CharField(max_length=128, blank=True)
    city                 = models.CharField(max_length=32)
    state                = us_models.USStateField()
    zip_code             = models.CharField(max_length=10,
                               validators=[RegexValidator(r'^\d{5}(-\d{4})?$')])
    date_registered      = models.DateTimeField(default=datetime.now()) 
    
class Child(models.Model):
    # Keyed Fields
    school = models.ForeignKey(School, null=True)
    family = models.ManyToManyField(Person, null=True)
    # Natural Fields
    first_name           = models.CharField(max_length=128)
    last_name            = models.CharField(max_length=128)
    
