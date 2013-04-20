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
 Last Update: 2013-04-20
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
def homepage(request):
    return render_to_response('homepage.html')


"""
 {
  Query Block
 }
 """
def search_business(request):
    return render_to_response('business.html')

def ajax_search_business(request, search_string):
    found = True 
    results = Business.objects.filter(name__startswith=search_string)
    if not results:
        results = Business.objects.all()
        found = False
    return render_to_response('render_album.html', {
                                "results": results,
                                "found": found,
                                })
    

def search_school(request):
    return render_to_response('school.html')

def ajax_search_school(request, search_string):
    found = True 
    results = School.objects.filter(name__startswith=search_string)
    if not results:
        results = School.objects.all()
        found = False
    return render_to_response('render_album.html', {
                                "results": results,
                                "found": found,
                                })
    

def search_person(request):
    return render_to_response('person.html')

def ajax_search_person(request, search_string):
    found = True 
    results = Person.objects.filter(last_name__startswith=search_string)
    if not results:
        results = Person.objects.all()
        found = False
    return render_to_response('render_album.html', {
                                "results": results,
                                "found": found,
                                })
    

def search_child(request):
    return render_to_response('child.html')

def ajax_search_child(request, search_string):
    found = True 
    results = Child.objects.filter(last_name__startswith=search_string)
    if not results:
        results = Child.objects.all()
        found = False
    return render_to_response('render_album.html', {
                                "results": results,
                                "found": found,
                                })
    

def search_global(request):
    return render_to_response('global.html')

def ajax_search_global(request, search_string):
    result_business = Business.objects.filter(name__startswith=search_string)
    result_school   = School.objects.filter(name__startswith=search_string)
    result_person   = Person.objects.filter(last_name__startswith=search_string)
    result_child    = Child.objects.filter(last_name__startswith=search_string)

    return render_to_response('render_album.html', {
                                "result_business": result_business,
                                "result_school": result_school,
                                "result_person": result_person,
                                "result_child": result_child,
                                })


"""
 {
  DISPLAY BLOCK
 }
 """    
def specific_business(request, offset):
    offset   = int(offset)
    business = Business.objects.get(pk=offset)
    people   = Person.objects.filter(business=business)
    return render_to_response('specific_business.html', locals())

def specific_school(request, offset):
    offset   = int(offset)
    school   = School.objects.get(pk=offset)
    children = Child.objects.filter(school=school)
    return render_to_response('specific_school.html', locals())

def specific_person(request, offset):
    offset = int(offset)
    person = Person.objects.get(pk=offset)
    return render_to_response('specific_person.html', locals())

def specific_child(request, offset):
    offset = int(offset)
    child  = Child.objects.get(pk=offset)
    return render_to_response('specific_child.html', locals())