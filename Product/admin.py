from django.contrib import admin

# Register your models here.
from Category.models import Category
from Product.models import Product
from Customer.models import Customer, Order, OrderDetail

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderDetail)