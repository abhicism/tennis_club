from django.urls import path #import (path)the url routing function used to map a URL to a view
from . import views  #import views.py from the same folder (current app)
 
urlpatterns = [     #dj looks for this list to know all routes of this app
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),    
]