from django.shortcuts import render
from .models import User
from .forms import Login
from django.views import View
from django.contrib import auth


class Login(View):
    def get(self, request):
        context = {'form_login': Login()}
        return render(request, 'user/login.html', context)

    def post(self, request):
        form = Login(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(user)
        else:
            context = {'form_login': Login()}
            return render(request, 'user/login.html', context)