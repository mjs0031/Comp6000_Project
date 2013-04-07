""" Python Package Imports """
from itertools import chain
from datetime import date, datetime, date, timedelta

""" Django Package Imports """
from django.db import models
from django.contrib.localflavor.us import models as us_models
from django.core import serializers
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db.models.query import QuerySet

""" Internal Package Imports """
# Not Applicable

"""

 Data_Base/models.py

 Author:      Matthew J Swann; 
              Yong Kin; 
              Bradon Atkins; and 
              Adam Carter
              
 Version:     1.0
 Last Update: 2013-04-07
 Update By:   Matthew J Swann
 
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
     Transforms the entire Business table to serialized xml. This is callable
     from any Business object and is ready for javascript API translation.
     """
    def table_to_string(self):
        query_to_xml(Business.objects.all())
    
        
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
     Transforms the entire school table to serialized xml. This is callable
     from any School object and is ready for javascript API translation.
     """
    def table_to_string(self):
        query_to_xml(School.objects.all())    


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
     Transforms the entire Person table to serialized xml. This is callable
     from any Person object and is ready for javascript API translation.
     """
    def table_to_string(self):
        query_to_xml(Person.objects.all())
    
    
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
     Transforms the entire Child table to serialized xml. This is callable
     from any Business object and is ready for javascript API translation.
     """
    def table_to_string(self):
        query_to_xml(Child.objects.all()) 
    
    
class OrderedChild(Child):
    class Meta:
        verbose_name        = "Ordered Child"
        verbose_name_plural = "Ordered Children"
        ordering            = ['last_name', 'first_name']
        proxy               = True
        
"""
 Serializes an entire query set into XML form and saves the file with a
 time-stamped name.
 
 @param query_set : Query set to be serialized. Arrives un-validated.
 
 @raise ValidationError: Raised if query_set is not of type QuerySet.
 """
def query_to_xml(query_set):
    if not isinstance(query_set, QuerySet):
        raise ValidationError('query_to_xml() requires type QuerySet')
    XMLSerializer  = serializers.get_serializer('xml')
    xml_serializer = XMLSerializer()
    timestamp      = datetime.now()
    path           = 'Control/fixtures/xml/%s_%s_%s_%s_%s_%s.xml' % ( timestamp.year,
                                                                      timestamp.month,
                                                                      timestamp.day,
                                                                      timestamp.hour,
                                                                      timestamp.minute,
                                                                      timestamp.second )
    output         = open(path, 'w')
    xml_serializer.serialize(query_set, stream=output)