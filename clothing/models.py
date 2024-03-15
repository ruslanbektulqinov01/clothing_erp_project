from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    GENDER_CHOICES = (['male', 'Male'],
                      ['female', 'Female'])
    category = models.CharField(max_length=100, choices=GENDER_CHOICES)
    size = models.CharField(max_length=50)
    COLORS_CHOICES = (
        ['white', 'White'], ['black', 'Black'], ['blue', 'Blue'], ['red', 'Red'],
        ['yellow', 'Yellow'], ['brown', 'Brown'], ['green', 'Green']
    )
    color = models.CharField(max_length=50, choices=COLORS_CHOICES)
    material = models.CharField(max_length=100)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField()
    minimum_stock_level = models.PositiveIntegerField()
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=255)
    address = models.TextField()
    tax_id = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    order_date = models.DateField()
    delivery_date = models.DateField()
    shipping_address = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    ORDER_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    order_status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES)

    def __str__(self):
        return f"{self.order_date}"


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    manager = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Stock(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    reorder_level = models.IntegerField()
    last_restocked_date = models.DateField()


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('transfer', 'Transfer'),
        ('adjustment', 'Adjustment'),
    )
    type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    from_warehouse = models.ForeignKey('Warehouse', related_name='from_transactions', on_delete=models.CASCADE)
    to_warehouse = models.ForeignKey('Warehouse', related_name='to_transactions', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.from_warehouse.name} - {self.to_warehouse}"


class Discounts(models.Model):
    DISCOUNT_TYPES = (
        ('percentage', 'Percentage'),
        ('fixed_amount', 'Fixed Amount'),
    )
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    discount_type = models.CharField(max_length=50, choices=DISCOUNT_TYPES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.discount_type} - {self.discount_value}"


class Payment(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.order} - {self.payment_date}"


class Returns(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    return_reason = models.TextField()
    return_date = models.DateField()


class ProductDetails(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)