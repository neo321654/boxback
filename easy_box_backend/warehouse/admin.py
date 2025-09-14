from django.contrib import admin
from .models import Item, Supplier, Movement

admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(Movement)
