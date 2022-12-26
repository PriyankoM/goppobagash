from django.contrib import admin
from .models.customer import Customer
from .models.category import Category
from .models.orders import Orders
from .models.products import Products
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(Products,AdminProduct)
