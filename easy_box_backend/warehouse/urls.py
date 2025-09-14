from django.urls import path
from .views import (
    UserListCreate,
    SupplierListCreate,
    LocationListCreate,
    ItemListCreate,
    MovementListCreate,
    OrderListCreate,
    OrderItemListCreate,
    StockReport,
)

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('suppliers/', SupplierListCreate.as_view(), name='supplier-list-create'),
    path('locations/', LocationListCreate.as_view(), name='location-list-create'),
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('movements/', MovementListCreate.as_view(), name='movement-list-create'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('order-items/', OrderItemListCreate.as_view(), name='order-item-list-create'),
    path('report/', StockReport.as_view(), name='stock-report'),
]
