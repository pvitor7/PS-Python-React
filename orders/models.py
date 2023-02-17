from django.db import models
import uuid
from products.models import Products
from users.models import User


class Orders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False)
    subtotal = models.DecimalField( max_digits=9, decimal_places=2, default=0)
    delivery = models.DecimalField( max_digits=9, decimal_places=2, default=0)
    total = models.DecimalField( max_digits=9, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

        

class OrderProducts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False, blank=False)
