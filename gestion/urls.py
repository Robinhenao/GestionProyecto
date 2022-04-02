from django.urls import path
from .views import gestion,manage_students,make_student,make_project,admin_project

urlpatterns = [
   path('', gestion, name="gestion_proyecto"),
   path('manage_project/manage_students', manage_students, name="manage_students"),
   path('manage_project/make_student', make_student, name="make_student"),
   path('manage_project/admin_project', admin_project, name="admin_project"),
   path('manage_project/make_project', make_project, name="make_project"),
   
   
]