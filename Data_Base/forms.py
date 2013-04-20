""" Python Package Support """
# Not Applicable

""" Django Package Support """
from django import forms
from django.contrib.localflavor.us.forms import USStateField 

""" Internal Package Imports """
from Control.choice_lists import SCHOOL_SET
from Data_Base.models import (Business, School,
                              Person,   Child)

"""

 Data_Base/forms.py

 Author:      Matthew J Swann; 
              Yong Kin; 
              Bradon Atkins; and 
              Adam Carter
              
 Version:     1.0
 Last Update: 2013-04-20
 Update By:   Matthew J Swann
 
 Code for the website forms and inherent functionality.

 """
 
 
"""
 BUSINESS Form
"""
class BusinessForm(forms.Form):
    name                 = forms.CharField(max_length=128)
    address_line_one     = forms.CharField(max_length=128)
    address_line_two     = forms.CharField(max_length=128, required=False)
    city                 = forms.CharField(max_length=32)
    state                = USStateField()
    zip_code             = forms.CharField(max_length=10)    
    phone                = forms.CharField(max_length=12, required=False)
    business_description = forms.CharField(widget=forms.Textarea)
    notes                = forms.CharField(widget=forms.Textarea)


"""
 SCHOOL Form
"""            
class SchoolForm(forms.Form):
    name             = forms.CharField(max_length=128)
    education_level  = forms.ChoiceField(choices=SCHOOL_SET, widget=forms.Select)
    address_line_one = forms.CharField(max_length=128)
    address_line_two = forms.CharField(max_length=128, required=False)
    city             = forms.CharField(max_length=32)
    state            = USStateField()
    zip_code         = forms.CharField(max_length=10)    
    phone            = forms.CharField(max_length=12, required=False)
    notes            = forms.CharField(widget=forms.Textarea)
 
        
"""
 PERSON Form
"""     
class PersonForm(forms.Form):
    first_name       = forms.CharField(max_length=128)
    last_name        = forms.CharField(max_length=128)
    business         = forms.ModelChoiceField(queryset=Business.objects.all())
    address_line_one = forms.CharField(max_length=128)
    address_line_two = forms.CharField(max_length=128, required=False)
    city             = forms.CharField(max_length=32)
    state            = USStateField()
    zip_code         = forms.CharField(max_length=10)  
      
"""
 CHILD Form
"""  
class ChildForm(forms.Form):
    first_name       = forms.CharField(max_length=128)
    last_name        = forms.CharField(max_length=128)
    school           = forms.ModelChoiceField(queryset=School.objects.all(), required=False)
    family           = forms.ModelMultipleChoiceField(queryset=Person.objects.all(), required=False)
