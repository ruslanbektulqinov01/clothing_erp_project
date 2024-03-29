# Generated by Django 5.0.3 on 2024-03-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0003_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('white', 'White'), ('black', 'Black'), ('blue', 'Blue'), ('red', 'Red'), ('yellow', 'Yellow'), ('brown', 'Brown'), ('green', 'Green')], max_length=50),
        ),
    ]
