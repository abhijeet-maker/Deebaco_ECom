from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import UserSignUpForm


@login_required
def home(request):
    print("You are not admin")
    return render(request, 'home.html')


@permission_required("admin")
def admin_home(request):
    print("You are admin")

    return render(request, 'admin_home.html')


def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        print("NotValid**********")
        print(form.data)
        if form.is_valid():
            print("True**********")
            form.save()
            # login(request, user)
            return redirect('E_Comm_User:login')
    else:
        print("False*********************")
        form = UserSignUpForm()

    context = {'form': form}

    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        role = User.objects.filter(username=user)
        print(role, "#################################")
        if user is not None:
            auth_login(request, user)
            return redirect('E_Comm_User:home')
            # return render(request, 'admin_home.html')
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('E_Comm_User:login')
