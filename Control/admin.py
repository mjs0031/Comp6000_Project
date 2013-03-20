""" Python Package Imports """
# Not Applicable

""" Django Package Imports """
from django.contrib import admin

"""     Internal Package Imports    """
""" ------------------------------- """
""" IMPORTED AT PACKAGE DESIGNATION """

"""

 Control/admin.py
 Author(s)    : Matthew J Swann; Yong Kin; Bradon Atkins
 Version      : 1.0
 Last Revised : 2013-02-17
 Update By    : Matthew J Swann
 
 Code for the Django admin site.
 
 """

class BusinessAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name', 'city', 'state', 'phone')
    list_filter   = ('state',)
    search_fields = ['name', 'city', 'state']
    ordering      = ['state', 'city']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('name', 'address_line_one', 'address_line_two',
                        'city', 'state', 'zip_code', 'phone',
                        'notes', 'business_description')
                 }),)
    
class PersonAdmin(admin.ModelAdmin):
    list_display  = ('id', 'last_name', 'first_name', 'state', 'business')
    list_filter   = ('state',)
    search_fields = ['last_name', 'city', 'state']
    ordering      = ['state', 'city', 'last_name']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('last_name', 'first_name', 'business', 'address_line_one', 'address_line_two',
                        'city', 'state', 'zip_code', 'date_registered')
                 }),)

class SchoolAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name', 'city', 'state')
    list_filter   = ('state',)
    search_fields = ['name', 'city', 'state']
    ordering      = ['state', 'city']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('name', 'address_line_one', 'address_line_two',
                        'city', 'state', 'zip_code', 'phone',
                        'notes', 'education_level')
                 }),)
    
class ChildAdmin(admin.ModelAdmin):
    list_display  = ('id', 'last_name', 'first_name', 'school')
    search_fields = ['last_name',]
    ordering      = ['last_name']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('last_name', 'first_name', 'school', 'family')
                 }),)

from Data_Base.models import (
    Business,
    School,
    Person,
    Child                     
        )
admin.site.register(Business, BusinessAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Child, ChildAdmin)