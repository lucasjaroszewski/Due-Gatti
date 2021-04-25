import json
import stripe
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCaptureRequest
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from apps.cart.cart import Cart
from apps.order.utils import checkout
from apps.order.models import Order
from apps.coupon.models import Coupon
from apps.shipping.models import Shipping
from . utilities import decrement_product_quantity, send_order_confirmation
from . models import Product

def create_checkout_session(request):
    data = json.loads(request.body)

    # Cupom BEGIN
    coupon_code = data['coupon_code']
    coupon_value = 0

    if coupon_code != '':
        coupon = Coupon.objects.get(code=coupon_code)

        if coupon.can_use():
            coupon_value = coupon.value
            coupon.use()

    # Cupom END

    # Shipping BEGIN
    shipping_code = data['shipping_code']
    shipping_value = 0

    if shipping_code != '':
        shipping = Shipping.objects.get(place=shipping_code)

        if shipping.can_ship():
            shipping_value = shipping.value

    # Shipping END

    cart = Cart(request)

    items = []
    for item in cart:
        product = item['product']
        price = int(product.price * 100)

        if coupon_value > 0:
            price = int(price * (int(coupon_value) / 100))

        obj = {
            'price_data': {
                'currency': 'brl',
                'product_data': {
                    'name': f'{product.title}'
                },
                'unit_amount': price
            },
            'quantity': item['quantity']
        }
        items.append(obj)

    # Total price of items
    total_price = 0.00

    for item in cart:
        product = item['product']
        total_price = total_price + (float(product.price) * int(item['quantity']))

    if coupon_value > 0:
        total_price = total_price * (coupon_value / 100)

    frete = {
        'price_data': {
            'currency': 'brl',
            'product_data': {
                'name': 'Frete para ' + shipping_code
            },
            'unit_amount': (shipping_value * 100)
        },
        'quantity': '1'
    }
    items.append(frete)

    taxa = {
        'price_data': {
            'currency': 'brl',
            'product_data': {
                'name': 'Taxa de Serviço: 3.99% + R$ 0,50'
            },
            'unit_amount': int((total_price + shipping_value) * 3.99 + 0.5 * 100)
        },
        'quantity': '1'
    }
    items.append(taxa)

    # Gateway
    gateway = data['gateway']
    session = ''
    order_id = ''
    payment_intent = 'ENTREGA'

    # Configuração do stripe BEGIN
    if gateway == 'stripe':
        stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            success_url='http://127.0.0.1:8000/carrinho/sucesso/',
            cancel_url='http://127.0.0.1:8000/carrinho/'
        )
        payment_intent = session.payment_intent

    # Criação do pedido STRIPE

    orderid = checkout(request, data['first_name'], data['email'], data['address'], data['zipcode'], data['place'], data['phone'], data['delivered_at'])

    # Configuração do stripe END

    order = Order.objects.get(pk=orderid)
    order.payment_intent = payment_intent
    order.paid_amount = total_price + shipping_value
    order.used_coupon = coupon_code
    order.place = shipping_code
    order.save()

    decrement_product_quantity(order)
    # send_order_confirmation(order)

    return JsonResponse({'session': session})

def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)

    return JsonResponse(jsonresponse)

def api_increment_quantity(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = data['product_id']

    cart = Cart(request)

    return JsonResponse(jsonresponse)

def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)

    return JsonResponse(jsonresponse)

# Pagamentos sem cartão de crédito
def api_checkout(request):

    cart = Cart(request)

    data = json.loads(request.body)


    jsonresponse = {'success': True}

    orderid = checkout(request, data['first_name'], data['email'], data['address'], data['zipcode'], data['place'], data['phone'], data['delivered_at'])

    order = Order.objects.get(pk=orderid)
    order.paid = False
    order.paid_amount = cart.get_total_cost()
    order.save()

    cart.clear()
    return JsonResponse(jsonresponse)
