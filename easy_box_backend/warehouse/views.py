from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item, Supplier, Movement
from .serializers import ItemSerializer, SupplierSerializer, MovementSerializer

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class SupplierListCreate(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class MovementListCreate(generics.ListCreateAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

class StockReport(APIView):
    def get(self, request, format=None):
        report = {}
        for item in Item.objects.all():
            report[item.name] = item.quantity
        return Response(report)