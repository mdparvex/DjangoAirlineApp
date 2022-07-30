from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
	path("", views.index, name="user_index"),
	path("login", views.login_view, name = "login"),
	path("logout", views.logout_view, name = "logout")
]