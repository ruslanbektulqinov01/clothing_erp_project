from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'suppliers', views.SupplierViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'order-items', views.OrderItemViewSet)
router.register(r'warehouses', views.WarehouseViewSet)
router.register(r'stocks', views.StockViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'discounts', views.DiscountsViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'returns', views.ReturnsViewSet)

urlpatterns = router.urls
