from django.urls import path
from .views import home, edit, delete, login_view, logout_view, register

urlpatterns = [
    path('',home, name='home'),
    path('edit/<int:id>/',edit, name='edit'),
    path('delete/<int:id>/',delete, name='delete'),
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout"),    
]
