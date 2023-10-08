from django.shortcuts import render
from django.views import View
from .models import Product, Category


# Create your views here.
class Home(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'shop/home.html', context)


class Product_slug(View):
    def get(self, request, cat_name):
        products = Product.objects.filter(category=cat_name)
        context = {'products': products}
        return render(request, 'shop/product_slug.html', context)
