""" Python Package Support """
# Not applicable

""" Django Package Support """
from django.conf.urls import patterns, include, url
from django.contrib import admin

""" Internal Package Support """
# Not applicable

"""
 Comp6000/urls.py
 Author:      Matthew J Swann
 Version:     1.0
 Last Update: 2013-03-20
 Update By:   Matthew J Swann
 
 
 URL settings

 """
 

admin.autodiscover()

urlpatterns = patterns('',
    
    # ADMIN PAGES
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
