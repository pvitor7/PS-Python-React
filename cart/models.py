from django.db import models
import uuid
from products.models import Products
from users.models import User


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)    
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartProducts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_products', null=False,  editable=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False,  editable=False)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    date_add = models.DateTimeField(auto_now_add=True)