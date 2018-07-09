"""dj_jot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views import generic
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

from apps.jwt_auth.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', generic.RedirectView.as_view(
        url='/api/', permanent=False)),
    path('api/', get_schema_view()),
    path('api/auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    path('users/actions/login', TokenObtainPairView.as_view()),
    
    path('', include(router.urls)),
    # Not in the spec, but it will almost certainly be needed
    # path('users/actions/refresh/', TokenRefreshView.as_view()),
]
