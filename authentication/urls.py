from django.urls import path
from authentication import views

urlpatterns = [
    path("", views.login_face, name="login_face"),
    path("register/", views.register, name="register"),
    path("login_password/", views.login_password, name="login_password"),
]