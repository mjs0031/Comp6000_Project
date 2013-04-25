""" Python Package Imports """
# Not Applicable

""" Django Package Imports """
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext

""" Internal Package Imports """
from Data_Base.models import (Business,     School,
                              Person,       Child,
                              query_to_xml)
from Data_Base.forms import  (BusinessForm, SchoolForm,
                              PersonForm,   ChildForm)

"""

 Data_base/views.py

 Author:      Matthew J Swann; 
              Yong Kin; 
              Bradon Atkins; and 
              Adam Carter
              
 Version:     1.0
 Last Update: 2013-04-25
 Update By:   Matthew J Swann
 
 Code for the website queries/control.
 
 AJAX queries to be run through HTML.
 To be contained in the 'templates' folder in Control.
 
 """

"""
 {
  ACCESS BLOCK
 }
 """
def homepage(request):
    return render_to_response('landing.html')


"""
 {
  COMMIT BLOCK
 }
 """
def commit_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            pointer = form.save_data()
            return HttpResponseRedirect('/business/%s' % (pointer.id))
    else:
        form = BusinessForm()
    return render(request, 'add_business.html', RequestContext(request, {
                                                    "form": form,                 
                                                        }))
    
def commit_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            pointer = form.save_data()
            return HttpResponseRedirect('/school/%s' % (pointer.id))
    else:
        form = SchoolForm()
    return render(request, 'add_school.html', RequestContext(request, {
                                                    "form": form,                 
                                                        }))
    
def commit_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            pointer = form.save_data()
            return HttpResponseRedirect('/person/%s' % (pointer.id))
    else:
        form = PersonForm()
    return render(request, 'add_person.html', RequestContext(request, {
                                                    "form": form,                 
                                                        }))

def commit_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            pointer = form.save_data()
            return HttpResponseRedirect('/child/%s' % (pointer.id))
    else:
        form = ChildForm()
    return render(request, 'add_child.html', RequestContext(request, {
                                                    "form": form,                 
                                                        }))


"""
 {
  QUERY BLOCK
 }
 """
def search_business(request):
    return render_to_response('search_business.html')

def ajax_search_business(request, search_string):
    found = True 
    results = Business.objects.filter(name__startswith=search_string)
    if not results:
        results = Business.objects.all()
        found = False
    return render_to_response('render_business.html', {
                                "results": results,
                                "found": found,
                                })
    

def search_school(request):
    return render_to_response('search_school.html')

def ajax_search_school(request, search_string):
    found = True 
    results = School.objects.filter(name__startswith=search_string)
    if not results:
        results = School.objects.all()
        found = False
    return render_to_response('render_school.html', {
                                "results": results,
                                "found": found,
                                })
    

def search_person(request):
    return render_to_response('search_person.html')

def ajax_search_person(request, search_string):
    found = True 
    results = Person.objects.filter(last_name__startswith=search_string)
    if not results:
        results = Person.objects.all()
        found = False
    return render_to_response('render_person.html', {
                                "results": results,
                                "found": found,
                                })
    

def search_child(request):
    return render_to_response('search_child.html')

def ajax_search_child(request, search_string):
    found = True 
    results = Child.objects.filter(last_name__startswith=search_string)
    if not results:
        results = Child.objects.all()
        found = False
    return render_to_response('render_child.html', {
                                "results": results,
                                "found": found,
                                })
    

def search_global(request):
    return render_to_response('search_global.html')

def ajax_search_global(request, search_string):
    found_b, found_s, found_p, found_c = True, True, True, True
    result_business = Business.objects.filter(name__startswith=search_string)
    result_school   = School.objects.filter(name__startswith=search_string)
    result_person   = Person.objects.filter(last_name__startswith=search_string)
    result_child    = Child.objects.filter(last_name__startswith=search_string)
    if (len(result_business) == 0):
        found_b = False
    if (len(result_school) == 0):
        found_s = False
    if (len(result_person) == 0):
        found_p = False
    if (len(result_child) == 0):
        found_c = False
    return render_to_response('render_global.html', {
                                "result_business": result_business,
                                "result_school": result_school,
                                "result_person": result_person,
                                "result_child": result_child,
                                "found_b": found_b,
                                "found_s": found_s,
                                "found_p": found_p,
                                "found_c": found_c,                                
                                })


"""
 {
  DISPLAY BLOCK
 }
 """    
def specific_business(request, offset):
    found    = True
    offset   = int(offset)
    business = Business.objects.get(pk=offset)
    people   = Person.objects.filter(business=business)
    if (len(people) == 0):
        found = False
    return render_to_response('specific_business.html', locals())

def specific_school(request, offset):
    found    = True
    offset   = int(offset)
    school   = School.objects.get(pk=offset)
    children = Child.objects.filter(school=school)
    if (len(children) == 0):
        found = False
    return render_to_response('specific_school.html', locals())

def specific_person(request, offset):
    offset = int(offset)
    person = Person.objects.get(pk=offset)
    return render_to_response('specific_person.html', locals())

def specific_child(request, offset):
    offset = int(offset)
    child  = Child.objects.get(pk=offset)
    return render_to_response('specific_child.html', locals())

"""
 {
  XML STREAM
 }
 """
def business_to_XML(request):
    business = Business.objects.get(pk=1)
    business.table_to_string()
    return render_to_response('landing.html')

def school_to_XML(request):
    school = School.objects.get(pk=1)
    school.table_to_string()
    return render_to_response('landing.html')

def person_to_XML(request):
    person = Person.objects.get(pk=1)
    person.table_to_string()
    return render_to_response('landing.html')

def child_to_XML(request):
    child = Child.objects.get(pk=1)
    child.table_to_string()
    return render_to_response('landing.html')