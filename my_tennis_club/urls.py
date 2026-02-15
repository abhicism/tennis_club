from django.contrib import admin  #import dj admin site
from django.urls import include, path  #path->define route, include ->forward to app urls

urlpatterns = [
    path('', include('members.urls')),  #when user visits root url "/" send request to member app urls.py
    # ' ' is empty string represent the root url (homepage) of website
    path('admin/', admin.site.urls),   #when user visits "/admin/" , open django admin panel (open dj admin interface)
]
