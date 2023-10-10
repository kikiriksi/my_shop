from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login', views.login, name='login'),
    path('reg', views.registration, name='reg'),
    path('profile', views.profile, name='profile'),

]
