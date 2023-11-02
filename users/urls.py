from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.signin, name="login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.signout, name="logout")
]
