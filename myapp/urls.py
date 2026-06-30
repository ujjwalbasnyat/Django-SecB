from django.contrib import admin
from django.urls import path
from . import views

# app_name ="blog"
urlpatterns = [
    path("create_post/", views.create_post, name="create_post"),
    path('', views.get_blog_post_view, name="home_view"),
    path('post_detail/<int:id>', views.post_detail_view, name="post_detail"),
    # signup url
    path('signup/', views.signup_view, name="signup"),
    path('logout/', views.logout_view, name="logout")
]