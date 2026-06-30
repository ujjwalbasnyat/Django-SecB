from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Blog
from .forms import CreatePostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# Create Blog Post
@login_required
def create_post(request):
    if request.method=="POST":
        post_form = CreatePostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('home_view')

    else:
        post_form = CreatePostForm()
    return render(request, "myapp/create_post.html",{"form": post_form})

# landing page view
def get_blog_post_view(request):
    posts = Blog.objects.all()

    return render(request, "myapp/base.html", {"posts": posts})


# post detail

def post_detail_view(request, id):
    post = Blog.objects.get(pk=id)

    return render(request, "myapp/post_detail.html", {"post": post})
    # return HttpResponse(post.content)

from .forms import SignupForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth import login


def signup_view(request):
    if request.method=="POST":
        form = SignupForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # form validation
            if password and confirm_password and password != confirm_password:
                raise forms.ValidationError("Password didn't match.")

            user = User.objects.create_user(username = username, password= password)
            user.save()

            login(request, user)

            return redirect("home_view")
    else:
        form = SignupForm()
    
    return render(request, "myapp/signup.html", {"form": form})

from django.contrib.auth import login, logout

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('signup')