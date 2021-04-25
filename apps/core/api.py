import json
import csv
import datetime
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from apps.order.models import Order
from apps.store.models import Product


def api_status_shipped(request):
    data = json.loads(request.body)
    order_id = str(data['order_id'])

    order = Order.objects.get(pk=order_id)
    order.status = 'shipped'
    order.save()

    return HttpResponse("Sucesso")

def api_status_ordered(request):
    data = json.loads(request.body)
    order_id = str(data['order_id'])

    order = Order.objects.get(pk=order_id)
    order.status = 'ordered'
    order.save()

    return HttpResponse("Sucesso")

def exportCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=Relatório' + str(datetime.datetime.now()) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['#', 'Adicionado em', 'Entrega em', 'Nome', 'Quantidade', 'Pedido'])

    orders = Order.objects.all()

    for order in orders:
        writer.writerow([order.id, order.created_at, order.delivered_at, order.first_name])

        for item in order.items.all():
            writer.writerow([item.quantity, item.product])

    return response
