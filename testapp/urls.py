from django.urls import path
from .views import *
urlpatterns=[
    path('examStart/',hello),
    path("startTest/",startTest),
]