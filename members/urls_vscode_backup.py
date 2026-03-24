from django.urls import path #import the 'path' function from django.urls
# Import the views module from the current app
# This allows us to access the view functions defined in views.py
from . import views
# urlpatterns is a list that stores all URL routes for this app
# Django checks this list to decide which view should handle a request
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet
router = DefaultRouter()
router.register('members', MemberViewSet)
urlpatterns = [
     path('members/', views.member_list),
    # '' represents the root URL of this app (example: http://127.0.0.1:8000/)
    # When a user visits the root URL, Django calls the 'main' view function
    # name='main' gives this URL a name so it can be referenced in templates
    path('', views.main, name='main'),
    # 'members/' is the URL path for the members page
    # When a user visits /members/, Django executes the 'members' view
    # This view will display the list of all members
    path('members/', views.members, name='members'),
    # 'members/' is the URL path for the members page
    # When a user visits /members/, Django executes the 'members' view
    # This view will display the list of all members
    path('members/details/<int:id>', views.details, name='details'),
     # 'testing/' is the URL for the testing page
    # Example: http://127.0.0.1:8000/testing/
    # When this URL is accessed, Django calls the 'testing' view function
    path('testing/', views.testing, name='testing'), 
    path('testing1/', views.testing1, name='testing1'),  
    path('testing2/', views.testing2, name='testing2'),  
    path('testing3/', views.testing3, name='testing3'),
    path('testing4/', views.testing4, name='testing4'),
    path('testing5/', views.testing5, name='testing5'),
    path('testing6/', views.testing6, name='testing6'),
    path('testing7/', views.testing7, name='testing7'),
    path('testing8/', views.testing8, name='testing8'),
    path('testing9/', views.testing9, name='testing9'),
    path('testing10/', views.testing10, name='testing10'),
    path('members/<int:id>/', views.member_detail),
     path('', include(router.urls)),
]