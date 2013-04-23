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
     Saves the current form data as a business.
     
     @return: Returns the newly created business object.
     """
    def save_data(self):
        pointer = Business.objects.create(
                    name                 = self.cleaned_data['name'],
                    address_line_one     = self.cleaned_data['address_line_one'],
                    address_line_two     = self.cleaned_data['address_line_two'],
                    city                 = self.cleaned_data['city'],
                    state                = self.cleaned_data['state'],
                    zip_code             = self.cleaned_data['zip_code'],
                    phone                = self.cleaned_data['phone'],
                    business_description = self.cleaned_data['business_description'],
                    notes                = self.cleaned_data['notes'],                  
                        )
        return pointer


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
     Saves the current form data as a school.
     
     @return: Returns the newly created school object.
     """
    def save_data(self):
        pointer = School.objects.create(
                    name                 = self.cleaned_data['name'],
                    education_level      = self.cleaned_data['education_level'],
                    address_line_one     = self.cleaned_data['address_line_one'],
                    address_line_two     = self.cleaned_data['address_line_two'],
                    city                 = self.cleaned_data['city'],
                    state                = self.cleaned_data['state'],
                    zip_code             = self.cleaned_data['zip_code'],
                    phone                = self.cleaned_data['phone'],
                    notes                = self.cleaned_data['notes'],                  
                        )
        return pointer
 
        
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
     Saves the current form data as a person.
     
     @return: Returns the newly created person object.
     """
    def save_data(self):    
        pointer = Person.objects.create(
                    first_name           = self.cleaned_data['first_name'],
                    last_name            = self.cleaned_data['last_name'],
                    business             = self.cleaned_data['business'],
                    address_line_one     = self.cleaned_data['address_line_one'],
                    address_line_two     = self.cleaned_data['address_line_two'],
                    city                 = self.cleaned_data['city'],
                    state                = self.cleaned_data['state'],
                    zip_code             = self.cleaned_data['zip_code'],                
                        )
        return pointer
    
      
"""
 CHILD Form
"""  
class ChildForm(forms.Form):
    first_name       = forms.CharField(max_length=128)
    last_name        = forms.CharField(max_length=128)
    school           = forms.ModelChoiceField(queryset=School.objects.all(), required=False)
    family           = forms.ModelMultipleChoiceField(queryset=Person.objects.all(), required=False)

    """
     Saves the current form data as a child.
     
     @return: Returns the newly created child object.
     """
    def save_data(self):
        pointer = Child.objects.create(
                    first_name = self.cleaned_data['first_name'],
                    last_name  = self.cleaned_data['last_name'],
                    school     = self.cleaned_data['school'],               
                        )
        for i in self.cleaned_data['family']:
            pointer.family.add(i)
        pointer.save()
        return pointer