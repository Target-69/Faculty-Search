from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.faculty_search, name='faculty_search'),
    path('contact/', views.contact, name='contact'),  # Define URL pattern for contact
]

