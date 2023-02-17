from .views import UserCreateView, LoginView, UserIdView # , UserDeactiveView, UserUpdatedView
from django.urls import path

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("users/", UserCreateView.as_view()),
    path("users/<pk>/", UserIdView.as_view()),
]   