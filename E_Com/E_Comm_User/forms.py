from django import forms
from django.contrib.auth.models import User


class UserSignUpForm(forms.ModelForm):
    # specify the name of model to use
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = "__all__"
        exclude = ("groups", "is_superuser", "last_login", "is_staff", "is_active")
