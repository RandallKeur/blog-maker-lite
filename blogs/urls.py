from django.contrib import admin
from django.urls import path

from blogs import views

app_name = "blogs"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs", views.blogs, name="blogs"),
    path("blogs/<int:blog_id>/", views.blog, name="blog"),
    path("posts/<int:post_id>/", views.post, name="post"),
    path("new_blog/", views.new_blog, name="new_blog"),
    path("new_post/<int:blog_id>/", views.new_post, name="new_post"),
    path("", views.index, name="index")
]
