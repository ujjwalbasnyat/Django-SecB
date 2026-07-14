from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import CreatePostForm
from django.contrib.auth.decorators import login_required
# from django.db import Q


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

from django.contrib.auth import login, logout, authenticate

@login_required
def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('signup')


def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home_view')
            else:
                raise forms.ValidationError("Invalid credentials.")
        else:
            return redirect("login")
        

    return render(request, 'myapp/login.html')

from django.db.models import Q
def search(request):
    if request.method=="GET":
        query = request.GET.get("query", "").strip()

        result = []

        contents = Blog.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query))
            

        # result.append()

        return render(request, "myapp/search.html", 
                      {
                          "query" : query,
                          "results" : contents
                      })

def edit(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    if request.method=="POST":
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post_id)
        
    else:
        form=CreatePostForm(instance=post)
    
    return render(request, 'myapp/edit_page.html', {"form": form})

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required
def settings(request):
    return render(request, "myapp/settings.html", {"user": request.user})

@login_required
def password_change(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success("password changes successfully.")
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, "myapp/password_change.html", {"form": form})