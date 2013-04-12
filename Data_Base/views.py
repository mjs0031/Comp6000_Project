""" Python Package Imports """
# Not Applicable

""" Django Package Imports """
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

""" Internal Package Imports """
from Data_Base.models import (Business, School,
                              Person,   Child)

"""

 Data_base/views.py

 Author:      Matthew J Swann; 
              Yong Kin; 
              Bradon Atkins; and 
              Adam Carter
              
 Version:     1.0
 Last Update: 2013-04-12
 Update By:   Matthew J Swann
 
 Code for the website queries/control.
 
 AJAX queries to be run through HTML.
 To be contained in the 'templates' folder in Control.
 
 """

"""
 {
  Access Block
 }
 """
def landing_page(request):
    return render_to_response('landing.html')

"""
 {
  Query Block
 }
 """
def search_business(request):
    return render_to_response('business.html')

def search_school(request):
    return render_to_response('school.html')

def search_person(request):
    return render_to_response('person.html')

def search_child(request):
    return render_to_response('child.html')

def search_global(request):
    return render_to_response('global.html')

