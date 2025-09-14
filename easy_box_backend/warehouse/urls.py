from django.urls import path
from .views import (
    ItemListCreate,
    SupplierListCreate,
    MovementListCreate,
    StockReport,
)

urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('suppliers/', SupplierListCreate.as_view(), name='supplier-list-create'),
    path('movements/', MovementListCreate.as_view(), name='movement-list-create'),
    path('report/', StockReport.as_view(), name='stock-report'),
]
