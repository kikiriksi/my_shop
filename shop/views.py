from django.shortcuts import render
from django.views import View

import user.views
from .models import Product, Category, Basket
from user.models import User
from django.http import HttpResponseRedirect


# Create your views here.
class Home(View):
    '''главная страница показывающая все категории'''

    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories}
        if request.user.username:
            context['baskets'] = Basket.objects.filter(user=request.user)
        return render(request, 'shop/home.html', context)


class Product_category_one(View):
    '''Показывает продукты в в выбранной категории'''

    def get(self, request, cat_name):
        products = Product.objects.filter(category=cat_name)
        context = {'products': products}
        return render(request, 'shop/product_slug.html', context)


def basket_add(request, product_id):
    '''Добовление товара в корзину'''
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
