from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q, Sum, Count
from apps.store.models import Product, Cat
from apps.order.models import Order, OrderItem
from django.utils import timezone
import datetime
import random

def frontpage(request):
    products = Product.objects.filter(is_featured=True).filter(parent=None)

    if len(products) >= 4:
        products = random.sample(products, 4)

    context = {
        'products': products,
    }

    return render(request, 'frontpage.html', context)

def products(request):
    # products = Product.objects.filter(variants=None).exclude(category=5)
    # Category = 5 (colheres)
    products = Product.objects.filter(parent=None)

    context = {
        'products': products
    }

    return render(request, 'products.html', context)

def gatos(request):
    cats = Cat.objects.all()

    context = {
        'cats': cats
    }
    return render(request, 'gatos.html', context)

def dashboard(request):
    recent_orders = Order.objects.all()[:4]

    # Dates
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    last_month = today.month - 1 if today.month > 1 else 12
    last_month_year = today.year if today.month > last_month else today.year - 1
    last_year = today.year - 1

    sales_today = Order.objects.filter(created_at__startswith=timezone.now().date()).aggregate(sum=Sum('paid_amount'))
    if sales_today['sum'] == None:
        sales_today['sum'] = 0

    sales_month = Order.objects.filter(created_at__year=today.year, created_at__month=today.month).aggregate(sum=Sum('paid_amount'))
    if sales_month['sum'] == None:
        sales_month['sum'] = 0

    sales_year = Order.objects.filter(created_at__year=today.year).aggregate(sum=Sum('paid_amount'))
    if sales_year['sum'] == None:
        sales_year['sum'] = 0

    sales_yesterday = Order.objects.filter(created_at=yesterday).aggregate(sum=Sum('paid_amount'))
    if sales_yesterday['sum'] == None:
        sales_yesterday['sum'] = 0

    daily_sales = ((sales_today['sum'] - sales_yesterday['sum']) / sales_yesterday['sum']) * 100

    sales_last_month = Order.objects.filter(created_at__year=last_month_year, created_at__month=last_month).aggregate(sum=Sum('paid_amount'))
    if sales_last_month['sum'] == None:
        sales_last_month['sum'] = sales_month['sum']

    monthly_sales = ((sales_month['sum'] - sales_last_month['sum']) / sales_last_month['sum']) * 100

    sales_last_year = Order.objects.filter(created_at__year=last_year).aggregate(sum=Sum('paid_amount'))
    if sales_last_year['sum'] == None:
        sales_last_year['sum'] = sales_year['sum']

    yearly_sales = ((sales_year['sum'] - sales_last_year['sum']) / sales_last_year['sum']) * 100



    most_sold = OrderItem.objects.values('product__parent__title').annotate(count=Count('product__parent__title')).order_by('-count')[:3]
    # most_sold = OrderItem.objects.values('product__parent__title').annotate(count=Count('product__parent__title')).order_by('-count')[:3]
    # most_sold = OrderItem.objects.annotate(product_count=Count('product'))

    #order_shipped = request.GET.get('status', 'shipped')

    context = {
        'recent_orders': recent_orders,
        'sales_yesterday': sales_yesterday,
        'sales_today': sales_today,
        'sales_month': sales_month,
        'sales_year': sales_year,
        'daily_sales': daily_sales,
        'monthly_sales': monthly_sales,
        'yearly_sales': yearly_sales,
        'most_sold': most_sold,
    }
    return render(request, 'dashboard.html', context)

def ordered_products(request):
    query = request.GET.get('query', '')
    orders = Order.objects.filter(Q(first_name__icontains=query) | Q(id__icontains=query)).filter(status='ordered')
    count_orders = Order.objects.all().count()
    count_shipped = Order.objects.filter(status__icontains='Shipped').count()
    count_ordered = Order.objects.filter(status__icontains='Ordered').count()
    sorting = request.GET.get('sorting', '-created_at')

    context = {
        'query': query,
        'orders': orders.order_by(sorting),
        'count_orders': count_orders,
        'count_shipped': count_shipped,
        'count_ordered': count_ordered,
        'sorting': sorting,
    }

    return render(request, 'ordered_products.html', context)

def shipped_products(request):
    query = request.GET.get('query', '')
    orders = Order.objects.filter(Q(first_name__icontains=query) | Q(id__icontains=query)).filter(status='shipped')
    count_orders = Order.objects.all().count()
    count_shipped = Order.objects.filter(status__icontains='Shipped').count()
    count_ordered = Order.objects.filter(status__icontains='Ordered').count()
    sorting = request.GET.get('sorting', '-created_at')

    context = {
        'query': query,
        'orders': orders.order_by(sorting),
        'count_orders': count_orders,
        'count_shipped': count_shipped,
        'count_ordered': count_ordered,
        'sorting': sorting,
    }

    return render(request, 'shipped_products.html', context)

def users_list(request):
    users = User.objects.all()
    count_users = User.objects.all().count()

    context = {
        'users': users,
        'count_users': count_users,
    }

    return render(request, 'users_list.html', context)

def allergens(request):
    allergens = Product.objects.filter(parent=None)

    context = {
        'allergens': allergens
    }
    return render(request, 'allergens.html', context)
