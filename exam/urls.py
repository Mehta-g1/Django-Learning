from django.urls import path
from .views import *
urlpatterns=[
    path('contact/',contact),
    path('about/',About),
    path('home/',Home),
    path('questions/',questions)
]