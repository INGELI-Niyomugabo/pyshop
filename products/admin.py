from django.contrib import admin
from .models import Item, Offer
# Register your models here.


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Item, ProductsAdmin)
admin.site.register(Offer, OfferAdmin)
