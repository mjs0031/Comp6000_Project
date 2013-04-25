""" Python Package Support """
# Not applicable

""" Django Package Support """
from django.conf.urls import patterns, include, url
from django.contrib import admin

""" Internal Package Support """
# Imported below.

"""
 Comp6000/urls.py
 Author:      Matthew J Swann
              Yong Kin; 
              Bradon Atkins; and 
              Adam Carter
              
 Version:     1.0
 Last Update: 2013-04-25
 Update By:   Matthew J Swann
 
 
 URL settings

 """

admin.autodiscover()

urlpatterns = patterns('',
    
    # ACCESS PAGES
    url(r'^$', 'Data_Base.views.homepage', name='homepage'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # COMMIT PAGES
    url(r'^commit/business/$', 'Data_Base.views.commit_business', name='commit_business'),
    url(r'^commit/school/$', 'Data_Base.views.commit_school', name='commit_school'),
    url(r'^commit/person/$', 'Data_Base.views.commit_person', name='commit_person'),
    url(r'^commit/child/$', 'Data_Base.views.commit_child', name='commit_child'),
    
    # SEARCH PAGES
    url(r'^search/business/$', 'Data_Base.views.search_business', name='search_business'),
    url(r'^search/school/$', 'Data_Base.views.search_school', name='search_school'),
    url(r'^search/person/$', 'Data_Base.views.search_person', name='search_person'),
    url(r'^search/child/$', 'Data_Base.views.search_child', name='search_child'),
    url(r'^search/global/$', 'Data_Base.views.search_global', name='search_global'),
    
    url(r'^search/business/(\w+)/$', 'Data_Base.views.ajax_search_business', name='ajax_search_business'),
    url(r'^search/school/(\w+)/$', 'Data_Base.views.ajax_search_school', name='ajax_search_school'),
    url(r'^search/person/(\w+)/$', 'Data_Base.views.ajax_search_person', name='ajax_search_person'),
    url(r'^search/child/(\w+)/$', 'Data_Base.views.ajax_search_child', name='ajax_search_child'),
    url(r'^search/global/(\w+)/$', 'Data_Base.views.ajax_search_global', name='ajax_search_global'),
    
    # DISPLAY PAGES
    url(r'^business/(\w+)/$', 'Data_Base.views.specific_business', name='specific_business'),
    url(r'^school/(\w+)/$', 'Data_Base.views.specific_school', name='specific_school'),
    url(r'^person/(\w+)/$', 'Data_Base.views.specific_person', name='specific_person'),    
    url(r'^child/(\w+)/$', 'Data_Base.views.specific_child', name='specific_child'),
    
    # AJAX QUERY OUTPUT
   url(r'^xml_business/$', 'Data_Base.views.business_to_XML', name='business_to_xml'),
   url(r'^xml_school/$', 'Data_Base.views.school_to_XML', name='school_to_xml'),
   url(r'^xml_person/$', 'Data_Base.views.person_to_XML', name='person_to_xml'),
   url(r'^xml_child/$', 'Data_Base.views.child_to_XML', name='child_to_xml'),

)
