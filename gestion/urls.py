from django.urls import path
from .views import delete_student,update_status,update_objetive, delete_objetivo,update_project,update_student, gestion, make_objective,manage_students,make_project,admin_project,delete_objetivoAdmin,delete_proyecto

urlpatterns = [
   path('', gestion, name="gestion_proyecto"),
   path('manage_project/admin_project/manage_students/<int:project_id>', manage_students, name="manage_students"),
   path('manage_project/admin_project/manage_students/delete_student/<int:numero_id>', delete_student, name="delete_student"),
   path('manage_project/admin_project/<int:project_id>', admin_project, name="admin_project"),
   path('manage_project/make_project', make_project, name="make_project"),
   path('manage_project/make_project/make_objective/<int:project_id>', make_objective, name="make_objective"),
   path('manage_project/make_project/make_objective/delete_objetivo/<int:objetive_id>',delete_objetivo, name="delete_objective"),
   path('manage_project/admin_project/update_project/<int:project_id>', update_project, name="update_project"),
   path('manage_project/admin_project/manage_students/update_student/<int:numero_id>', update_student, name="update_student"),
   path('manage_project/admin_project/update_status/<int:objetive_id>', update_status, name="update_status"),
   path('manage_project/admin_project/update_objetive/<int:objetive_id>', update_objetive, name="update_objetive"),
   path('manage_project/admin_project/delete_objetivoAdmin/<int:objetive_id>',delete_objetivoAdmin, name="delete_objetivoAdmin"),
   path('manage_project/admin_project/delete_proyecto/<int:project_id>',delete_proyecto, name="delete_proyecto")
]