import os
import datetime
from random import randint
from apps.cart.cart import Cart
from apps.order.models import Order, OrderItem

def checkout(request, first_name, email, address, zipcode, place, phone, delivered_at):
    order = Order(first_name=first_name, email=email, address=address, zipcode=zipcode, place=place, phone=phone, delivered_at=delivered_at)

    if request.user.is_authenticated:
        order.user = request.user

    order.save()

    cart = Cart(request)

    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

    return order.id
