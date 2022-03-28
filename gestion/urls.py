from django.urls import path
from .views import gestion

urlpatterns = [
   path('gestion_proyecto/', gestion, name="gestion_proyecto"),
   
]