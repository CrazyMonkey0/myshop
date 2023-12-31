"""
URL configuration for myshop project.
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.urls import path, include

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path(_('orders/'), include('orders.urls', namespace='orders')),
    path(_('cart/'), include('cart.urls', namespace='cart')),
    path(_('coupons/'), include('coupons.urls', namespace='coupons')),
    path('rosetta/', include('rosetta.urls')),
    path('', include('shop.urls', namespace='shop')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
