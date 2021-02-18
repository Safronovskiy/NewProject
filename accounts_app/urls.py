from django.urls import path, include
from .views import *



app_name='accounts'

urlpatterns = [
    path('registration/', registration, name='register'),
    path('login/', CustomUserLogin.as_view(), name='login'),

    path('logout/', CustomUserLogout.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('editprofile/', edit_profile, name='editprofile'),
    ]




