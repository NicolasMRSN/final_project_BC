from django.urls import path
from authentication import views

urlpatterns = [
    path("", views.login_password, name="login_password"),
    path("users/", views.users_list, name="users_list"),
    path("users/<int:pk>/", views.user_view, name="user_view"),
]
