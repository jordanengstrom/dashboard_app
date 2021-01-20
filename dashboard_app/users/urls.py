from django.urls import path
from .views import (register, login, logout, AuthenticatedUser,
                    PermissionAPIView)


urlpatterns = [
    # path('users', users_view),
    path('register', register),
    path('login', login),
    path('logout', logout),
    path('user', AuthenticatedUser.as_view()),
    path('permissions', PermissionAPIView.as_view()),
]
