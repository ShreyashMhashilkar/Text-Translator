from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.translator,name='translator'),
    path('translated/',views.translated, name="translated")
]