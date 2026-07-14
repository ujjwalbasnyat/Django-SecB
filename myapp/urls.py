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
    path('logout/', views.logout_view, name="logout"),

    path('login/', views.login_view, name="login"),

    path('search/', views.search, name="search"),

    path('blog/<int:post_id>/edit', views.edit, name="edit"),
    path('change_password/', views.password_change, name="password_change"),
    path('settings/', views.settings, name="settings")
]