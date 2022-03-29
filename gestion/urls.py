from django.urls import path
from .views import gestion

urlpatterns = [
   path('', gestion, name="gestion_proyecto"),
   
]