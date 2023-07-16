import http
import os

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.db.models import F

from Shop_project import settings
from shop.models import Category, Product
from cart.views import CartAddProductForm


# Create your views here.


def env(request):
    return render(request, "environment.html", {"env": os.environ,
                                                "Django_env": settings.env})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  'shop/product/list.html',
                  {"category": category,
                   "categories": categories,
                   "products": products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


# TODO удалить позже, создал что бы посмотреть как работает HttpResponse
def create_new_categ(request, name):
    new_cat = Category.custom_manager.create_stupid_categ(name)

    return HttpResponse(status=http.HTTPStatus.OK, content=f"category with name ={new_cat} was created")


def show_sql(request):
    return HttpResponse(status=http.HTTPStatus.OK,
                    content=f"first : {Category.objects.filter(products__name__contains='Lennon').filter(products__created__year=F('products__updated__year')).query} \n \
                                second: {Category.objects.filter(products__name__contains='Lennon', products__created__year=2008).query} ")
