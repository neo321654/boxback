from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Supplier, Location, Item, Movement, Order, OrderItem
from .serializers import UserSerializer, SupplierSerializer, LocationSerializer, ItemSerializer, MovementSerializer, OrderSerializer, OrderItemSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SupplierListCreate(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class LocationListCreate(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class MovementListCreate(generics.ListCreateAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemListCreate(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class StockReport(APIView):
    def get(self, request, format=None):
        report = {}
        for item in Item.objects.all():
            report[item.name] = item.quantity
        return Response(report)
