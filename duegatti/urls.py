from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views

from apps.core.views import frontpage, gatos, products, dashboard, allergens, ordered_products, shipped_products, users_list
from apps.store.views import product_detail, category_detail, search
from apps.cart.views import cart_detail, success
from apps.order.views import admin_order_pdf
from apps.userprofile.views import signup, myaccount
from apps.cart.webhook import webhook
from apps.coupon.api import api_can_use
from apps.shipping.api import api_can_ship
from apps.store.api import api_add_to_cart, api_remove_from_cart, api_checkout, create_checkout_session
from apps.newsletter.api import api_add_subscriber
from apps.core.api import api_status_ordered, api_status_shipped, exportCSV

from . sitemaps import StaticViewSitemap, CategorySitemap, ProductSitemap

sitemaps = {'static': StaticViewSitemap, 'product': ProductSitemap, 'category': CategorySitemap}

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('procurar/', search, name='search'),
    path('cardapio/', products, name='products'),
    path('carrinho/', cart_detail, name='cart'),
    path('hooks/', webhook, name='webhook'),
    path('carrinho/sucesso/', success, name='success'),
    path('mural/', gatos, name='mural'),
    path('alergicos/', allergens, name='allergens'),

    # Admin acima dos API e Produtos
    path('admin/', admin.site.urls),
    path('admin/admin_order_pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),

    # Autenticação
    path('minhaconta/', myaccount, name='myaccount'),
    path('registrar/', signup, name='signup'),
    path('entrar/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', views.LogoutView.as_view(), name='logout'),

    # Sitemaps
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),
    path('pedidos/agendados/', ordered_products, name='ordered_products'),
    path('pedidos/entregues/', shipped_products, name='shipped_products' ),
    path('usuarios/', users_list, name='users_list'),
    path('export-csv/', exportCSV, name='export-csv'),

    # API
    path('api/can_ship/', api_can_ship, name='api_can_use'),
    path('api/can_use/', api_can_use, name='api_can_use'),
    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    path('api/checkout/', api_checkout, name='api_checkout'),
    path('api/add_subscriber/', api_add_subscriber, name='api_add_subscriber'),
    path('api/status_shipped/', api_status_shipped, name='api_status_shipped'),
    path('api/status_ordered/', api_status_ordered, name='api_status_ordered'),

    # Produtos
    path('cardapio/<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('cardapio/<slug:slug>/', category_detail, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
