from django.urls import path
from .views import *


app_name='main_app'

urlpatterns = [
        path('posts/', blogposts, name='allposts'),
        path('posts/add/', addpost, name='addpost'),
        path('posts/editpost/<int:pk>', editpost, name='editpost'),
        path('posts/deletepost/<int:pk>', delpost, name='delpost'),
        path('cats/', blogcats, name='blogcats'),
        path('cats/add/',addcat, name='addcat'),
        path('cats/edit/<int:pk>', editcat, name='editcat'),
        path('cats/delete/<int:pk>', deletecat, name='delcat'),
        path('', startpage, name='startpage'),
    ]



