# coding: utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from apps.accounts.forms import RegistrationForm


def login_view(request):
    arg = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/index/')
            else:
                arg = {'login_error': 'Пользователь не найден э'}
        else:
            arg = {'login_error': 'Чет не правильно'}
    return render(request, 'accounts/login.html', arg)


def logout_view(request):
    logout(request)
    return redirect('/index/')


def registration_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.set_password(request.POST['password'])
        user.save()
        return redirect('/index/')
    return render(request, 'accounts/registration.html', {'form': form})
