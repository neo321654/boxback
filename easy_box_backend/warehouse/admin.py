from django.contrib import admin
from .models import User, Supplier, Location, Item, Movement, Order, OrderItem

admin.site.register(User)
admin.site.register(Supplier)
admin.site.register(Location)
admin.site.register(Item)
admin.site.register(Movement)
admin.site.register(Order)
admin.site.register(OrderItem)
