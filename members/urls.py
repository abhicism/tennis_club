from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'viewset-members', views.MemberViewSet, basename='member-viewset')

urlpatterns = [
    path('', views.main, name='main'),
    path('members-page/', views.members, name='members'),
    path('members/details/<int:id>/', views.details, name='details'),
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
    path('api/members/', views.members_list, name='api-members-list'),
    path('api/members/<int:id>/', views.member_detail, name='api-member-detail'),
    path('api/', include(router.urls)),
]