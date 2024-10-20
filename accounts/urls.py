from django.contrib.auth import urls as auth_urls
from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    path("", include(auth_urls))
]
