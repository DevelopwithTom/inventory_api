from django.contrib import admin
from core.models import Product

# class ProductAdmin(admin.ModelAdmin):
#     list_display=[
#         "sku",
#         "name",
#         "quantity",
#         "price",
       
        
#     ]
 

admin.site.register(Product)
