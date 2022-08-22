from django.urls import path

from . import views

app_name = 'E_Comm_User'

urlpatterns = [
    path('', views.login, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.signup, name='signUp'),
    path('login/', views.login, name='login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    # path('placements/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
]
