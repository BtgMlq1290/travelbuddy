#Urls.py
#------------------------------------------------------------------------------------------------

'''This is the urls.py page for the app travels. This connects to the app views.'''

from django.conf.urls import url
from . import views

urlpatterns = [

    #This is the urls connecting to the name via reverse, Connected here at the apps url to the views
    url(r'^create$', views.create, name = 'travels_create'),
    url(r'^join$', views.join, name = 'travels_join'),
    url(r'^createtravel$', views.createtravel, name = 'travels_createtravel'),


    #?P creates a named group
    #<id> is the id
    #\d is a character group and the + is a quantifier only 1 or more digits will matc
    url(r'^(?P<id>\d+)$', views.travels, name = 'login_travels'),
    url(r'^show/(?P<id>\d+)$', views.show, name="travels_show"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="travels_remove")
    
]
