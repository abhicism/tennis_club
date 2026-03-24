from django.contrib import admin  # import dj admin site
from django.urls import include, path  # path -> define route, include -> forward to app urls

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', include('members.urls')),  # root → members app
    path('admin/', admin.site.urls),   # admin panel

    # ✅ JWT Authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]