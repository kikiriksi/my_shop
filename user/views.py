from django.shortcuts import render, redirect, reverse
from .models import User
from .forms import Login, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from shop.models import Basket


def login(request):
    '''авторизация пользователя'''
    if request.method == 'POST':
        form = Login(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
        else:
            context = {'form_login': Login(data=request.POST)}
            return render(request, 'user/login.html', context)
    else:
        context = {'form_login': Login()}
        return render(request, 'user/login.html', context)


def registration(request):
    '''Регистрация пользователя'''
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация успешна!!!')
            return redirect('user:login')
        else:
            form = UserRegistrationForm(data=request.POST)
            return render(request, 'user/registration.html', context={'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'user/registration.html', context={'form': form})


def profile(request):
    '''Изменения данных пользователя'''
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:profile')
    else:
        form = UserProfileForm(instance=request.user)
        return render(request, 'user/profile.html', context={'form': form,
                                                             'bascet': Basket.objects.all()})


def logout(request):
    '''выход пользователя из профиля'''
    auth.logout(request)
    return redirect('home')
