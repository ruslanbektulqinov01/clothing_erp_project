from rest_framework import viewsets
from .models import Product, Supplier, Customer, Order, OrderItem, Warehouse, Stock, Transaction, Discounts, Payment, Returns
from .serializers import ProductSerializer, SupplierSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer, WarehouseSerializer, StockSerializer, TransactionSerializer, DiscountsSerializer, PaymentSerializer, ReturnsSerializer
from rest_framework.authentication import SessionAuthentication


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication]

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    authentication_classes = [SessionAuthentication]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [SessionAuthentication]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication]

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    authentication_classes = [SessionAuthentication]


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    authentication_classes = [SessionAuthentication]

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    authentication_classes = [SessionAuthentication]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [SessionAuthentication]

class DiscountsViewSet(viewsets.ModelViewSet):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer
    authentication_classes = [SessionAuthentication]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = [SessionAuthentication]

class ReturnsViewSet(viewsets.ModelViewSet):
    queryset = Returns.objects.all()
    serializer_class = ReturnsSerializer
    authentication_classes = [SessionAuthentication]
