from django.contrib import admin
from SHOP.models import TradeMark, Products, ModelType, GadgetType


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'trade_mark', 'model_type', 'gadget_type')
    search_fields = ('name', 'trade_mark__name', 'model_type__name')


admin.site.register(TradeMark)
admin.site.register(Products, ProductAdmin)
admin.site.register(ModelType)
admin.site.register(GadgetType)
