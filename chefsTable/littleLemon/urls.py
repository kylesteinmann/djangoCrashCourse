from django.contrib import admin
from django.urls import path
from . import views

uropatterns = [
    path('',views.hello, name='hello'), 
    path('menu/<int:menu_id>', views.menu_by_id, name='menu_by_id'),
    ] 