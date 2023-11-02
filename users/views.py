from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CustomLoginForm, RegisterForm, ChangePasswordForm
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from django.contrib.auth.decorators import login_required


def signin(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = CustomLoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('profile')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {"form": form})


@login_required(login_url='login')
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            messages.success(
                request, 'Your password was successfully changed.')
            return redirect('profile')

    else:
        form = ChangePasswordForm(request.user)

    return render(request, 'profile.html', {"form": form, "name": user.name})


def signout(request):
    logout(request)
    return redirect('login', )
