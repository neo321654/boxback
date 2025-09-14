from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=50)

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='items_created')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Movement(models.Model):
    MOVEMENT_TYPE_CHOICES = (
        ('income', 'Income'),
        ('outcome', 'Outcome'),
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=50, choices=MOVEMENT_TYPE_CHOICES)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movement_type} of {self.quantity} {self.item.name}'

class Order(models.Model):
    ORDER_TYPE_CHOICES = (
        ('purchase', 'Purchase'),
        ('sale', 'Sale'),
    )
    order_type = models.CharField(max_length=50, choices=ORDER_TYPE_CHOICES)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders_created')
    status = models.CharField(max_length=50, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.item.name} for Order {self.order.id}'
