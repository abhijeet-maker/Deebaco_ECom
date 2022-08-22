from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
urlpatterns = [
    path('getload/', views.getload),
]
