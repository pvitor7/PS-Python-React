# Generated by Django 4.1.6 on 2023-02-17 05:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OrderProducts",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("quantity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "subtotal",
                    models.DecimalField(decimal_places=2, default=0, max_digits=9),
                ),
                (
                    "delivery",
                    models.DecimalField(decimal_places=2, default=0, max_digits=9),
                ),
                (
                    "total",
                    models.DecimalField(decimal_places=2, default=0, max_digits=9),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
