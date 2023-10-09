from django.urls import path
from . import views
urlpatterns = [
    path('', views.ass, name='ass'),

]