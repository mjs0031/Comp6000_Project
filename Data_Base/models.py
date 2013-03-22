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
 Author(s)    : Matthew J Swann; Yong Kin; Bradon Atkins; Adam Carter
 Version      : 1.0
 Last Revised : 2013-03-22
 Update By    : Matthew J Swann
 
 Code for the database tables and inherent functionality.

 """

SCHOOL_SET = (
    ('P', 'Primary'),
    ('S', 'Secondary'),
    ('C', 'Continuing Education'),
        ) 
 
"""
 BUSINESS Class --
 """
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
    
    def __unicode__(self):
        return '%s, %s, %s' % (self.name, self.city, self.state)
    
    class Meta:
        verbose_name        = "Business"
        verbose_name_plural = "Businesses"
        
        
    """
     Converts the current Business object to string form for XML storage.
     
     @param param: 
     
     @return: 
     
     @raise exception: 
     """
    def to_string(self):
        # Turns a Business object into string for XML storage
        pass
    
        
class OrderedBusiness(Business):
    class Meta:
        verbose_name        = "Ordered Business"
        verbose_name_plural = "Ordered Businesses"
        ordering            = ['state', 'name']
        proxy               = True


"""
 SCHOOL Class --
 """    
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
    
    def __unicode__(self):
        return '%s, %s, %s, %s' % (self.name, self.education_level,self.city, self.state)
    
    class Meta:
        verbose_name        = "School"
        verbose_name_plural = "Schools"
        
        
    """
     Converts the current School object to string form for XML storage.
     
     @param param: 
     
     @return: 
     
     @raise exception: 
     """
    def to_string(self):
        # Turns a School object into string for XML storage
        pass
    

class OrderedSchool(School):
    class Meta:
        verbose_name        = "Ordered School"
        verbose_name_plural = "Ordered Schools"
        ordering            = ['state', 'name']
        proxy               = True


"""
 PERSON Class --
 """    
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
    
    
    def __unicode__(self):
        name = '%s, %s:' % (self.last_name, self.first_name)
        return '%s, %s' % (name, self.date_registered)
    
    class Meta:
        verbose_name        = "Person"
        verbose_name_plural = "People"
        
        
    """
     Converts the current Person object to string form for XML storage.
     
     @param param: 
     
     @return: 
     
     @raise exception: 
     """
    def to_string(self):
        # Turns a Person object into string for XML storage
        pass
    
    
class OrderedPerson(Person):
    class Meta:
        verbose_name        = "Ordered Person"
        verbose_name_plural = "Ordered People"
        ordering            = ['last_name', 'first_name']
        proxy               = True
    
    
"""
 CHILD class --
 """
class Child(models.Model):
    # Keyed Fields
    school = models.ForeignKey(School, null=True)
    family = models.ManyToManyField(Person, null=True)
    # Natural Fields
    first_name           = models.CharField(max_length=128)
    last_name            = models.CharField(max_length=128)
    
    
    def __unicode__(self):
        name = '%s, %s:' % (self.last_name, self.first_name)
        return '%s' % (name)
    
    class Meta:
        verbose_name        = "Child"
        verbose_name_plural = "Children"
        
        
    """
     Converts the current Child object to string form for XML storage.
     
     @param param: 
     
     @return: 
     
     @raise exception: 
     """
    def to_string(self):
        # Turns a Child object into string for XML storage
        pass
 
    
class OrderedChild(Child):
    class Meta:
        verbose_name        = "Ordered Child"
        verbose_name_plural = "Ordered Children"
        ordering            = ['last_name', 'first_name']
        proxy               = True