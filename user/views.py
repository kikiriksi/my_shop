from django.shortcuts import render, redirect
from .models import User
from .forms import Login
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
