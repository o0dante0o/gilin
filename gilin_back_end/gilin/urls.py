from .views import *
from django.urls import path


urlpatterns = [
    path('country/add/',add_country , name='add-country'),
]
