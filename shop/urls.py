from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<str:cat_name>', views.Product_slug.as_view(), name='product_slug')

]