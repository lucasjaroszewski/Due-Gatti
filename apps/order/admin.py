import datetime
from django.contrib import admin
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from . models import Order, OrderItem

def order_name(obj):
    return '%s' % (obj.first_name)
order_name.short_description = 'Name'

def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('admin_order_pdf', args=[obj.id])))
order_pdf.short_description = 'PDF Order'

def admin_order_shipped(modeladmin, request, queryset):
    for order in queryset:
        order.shipped_date = datetime.datetime.now()
        order.status = Order.SHIPPED
        order.save()

        html = render_to_string('order_sent.html', {'order': order})
        send_mail('Pedido enviado', 'Seu pedido foi enviado!', 'duegattibot@gmail.com', ['ljnunes@outlook.com.br', order.email], fail_silently=False, html_message=html)
    return
admin_order_shipped.short_description = 'Set shipped'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', order_name, 'paid_amount', 'paid', 'status', 'created_at', 'delivered_at', order_pdf]
    list_filter = ['created_at', 'status']
    search_fields = ['first_name', 'address']
    inlines = [OrderItemInline]
    actions = [admin_order_shipped]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
