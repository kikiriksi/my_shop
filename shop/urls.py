from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<str:cat_name>', views.Product_category_one.as_view(), name='Product_category_one')

]