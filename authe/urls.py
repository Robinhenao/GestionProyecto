from django.urls import path
from .views import login_session,logout_session

urlpatterns = [
    path('login/', login_session, name="login"),
    path('logoutsession/', logout_session, name="logoutsession")
]