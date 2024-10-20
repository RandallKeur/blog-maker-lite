from django.contrib.auth import urls as auth_urls
from django.urls import path, include

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path("", include(auth_urls)),
    path("register/", views.register, name="register"),
]
