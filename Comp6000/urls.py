""" Python Package Support """
# Not applicable

""" Django Package Support """
from django.conf.urls import patterns, include, url
from django.contrib import admin

""" Internal Package Support """
from Data_Base.views import (landing_page, search_global,
                             search_business, search_school,
                             search_person, search_child)

"""
 Comp6000/urls.py
 Author:      Matthew J Swann
              Yong Kin; 
              Bradon Atkins; and 
              Adam Carter
              
 Version:     1.0
 Last Update: 2013-04-12
 Update By:   Matthew J Swann
 
 
 URL settings

 """

admin.autodiscover()

urlpatterns = patterns('',
    
    # ADMIN PAGES
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # ACCESS PAGES
    url(r'^$', landing_page),
    
    # SEARCH PAGES
    url(r'^search/business/$', search_business),
    url(r'^search/school/$', search_school),
    url(r'^search/person/$', search_person),
    url(r'^search/child/$', search_child),
    url(r'^search/global/$', search_global),
)
