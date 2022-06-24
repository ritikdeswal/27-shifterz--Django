from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('product/<int:n>', views.product_page),
    path('del-user/', views.del_user),


    path('getaddress/', views.getaddress),
    path('newaddress/', views.add_address),
    path('deleteaddress/<int:n>', views.deleteaddress),

    path('getwishlist/', views.getwishlist),
    path('addwishlist/<int:n>', views.addwishlist),
    path('removewishlist/<int:n>', views.removewishlist),

    path('getorders/', views.getorders),

    path('cart/', views.cart),
    path('add-to-cart/<int:n>', views.add_to_cart),
    path('remove-from-cart/<int:n>', views.remove_from_cart),
    path('minus-cart/<int:n>', views.minus_cart),
    path('plus-cart/<int:n>', views.plus_cart),

    path('checkout/', views.checkout),
    path('handlerequest/', views.handlerequest),
    path('success/<int:n>', views.success),

    path('privacy/', views.privacy),
    path('terms/', views.terms),
    path('return-policy/', views.returnpolicy),
    path('shipping-policy/', views.shippingpolicy),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)