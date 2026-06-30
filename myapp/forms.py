from django import forms
from .models import Blog

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blog

        fields = [
            "title", "author", "content", "category"
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Enter title",
                    "class": "form-control"
                    }),
            "author": forms.TextInput(
                attrs={
                    "placeholder": "enter author name",
                    # "max_length": 20,
                    # "readonly": False
                }
            ),
            "content" : forms.Textarea(
                attrs={
                    "row": 6,
                    "placeholder": "Enter your blog content.."
                }
            ),
            "category" : forms.TextInput(
                attrs={
                    "placeholder": 'enter category'
                }
            )
        }

from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']

    