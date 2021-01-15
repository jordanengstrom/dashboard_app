from django.urls import path
from .views import users_view, register, login, AuthenticatedUser


urlpatterns = [
    path('users', users_view),
    path('register', register),
    path('login', login),
    path('user', AuthenticatedUser.as_view())
]
