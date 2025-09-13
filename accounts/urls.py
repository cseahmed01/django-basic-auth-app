from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # login/register page
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.user_logout, name='logout'),
]
