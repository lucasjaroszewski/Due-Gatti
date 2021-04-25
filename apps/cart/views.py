from django.shortcuts import render
from django.conf import settings
from . cart import Cart
from apps.shipping.models import Shipping

def cart_detail(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        url = '/cardapio/%s/%s/' % (product.category.slug, product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'url': '%s', 'num_available': '%s', 'parent': '%s', 'spoon_available': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'], product.thumbnail.url, url, product.num_available, product.parent, product.spoon.num_available)

        productsstring = productsstring + b

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
    else:
        first_name = last_name = email = ''

    shippings = Shipping.objects.all()

    context = {
        'cart': cart,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'pub_key': settings.STRIPE_API_KEY_PUBLISHABLE,
        'pub_key_paypal': settings.PAYPAL_API_KEY_PUBLISHABLE,
        'productsstring': productsstring.rstrip(','),
        'shippings': shippings
    }
    return render(request, 'cart.html', context)

def success(request):
    cart = Cart(request)
    cart.clear()

    return render(request, 'success.html')
