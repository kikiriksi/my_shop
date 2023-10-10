from django.shortcuts import render, redirect
from .models import User
from .forms import Login, UserRegistrationForm, UserProfileForm
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        form = Login(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('home')
    else:
        context = {'form_login': Login()}
        return render(request, 'user/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
    else:
        form = UserRegistrationForm()
        return render(request, 'user/registration.html', context={'form': form})


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:profile')
    form = UserProfileForm(instance=request.user)
    return render(request, 'user/profile.html', context={'form': form})
