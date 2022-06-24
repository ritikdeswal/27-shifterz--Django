from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced,
    Wishlist
)
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','description','brand','category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','wish']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','order_id','amount','ordered_date','status']

    # def customer_info(self,obj):
    #     link=reverse("admin:app_customer_change", args=[obj.customer.pk])
    #     return format_html('<a href="{}">{}</a>',link,obj.customer.name)

    # def product_info(self,obj):
    #     link=reverse("admin:app_product_change", args=[obj.product.pk])
    #     return format_html('<a href="{}">{}</a>',link,obj.product.title)
