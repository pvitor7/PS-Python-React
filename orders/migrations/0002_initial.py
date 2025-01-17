# Generated by Django 4.1.6 on 2023-02-17 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0001_initial"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="user",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="orderproducts",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="orders.orders"
            ),
        ),
        migrations.AddField(
            model_name="orderproducts",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="products.products"
            ),
        ),
    ]
