from django.test import TestCase
from .models import Cart, CartProducts
from products.models import Products
from users.models import User
from django.db.utils import IntegrityError, DataError

from datetime import datetime


class CartProductsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='john', email='john@example.com', cellphone='123456789')
        self.cart = Cart.objects.create(user=self.user, is_finished=False)
        self.product = Products.objects.create(name='Test Product', price=10.99, score=5, image='test.png')

    def test_create_cart_product_with_correct_fields(self):
        cart_product = CartProducts.objects.create(cart=self.cart, product=self.product, quantity=3)
        self.assertIsInstance(cart_product, CartProducts)
        self.assertEqual(cart_product.cart, self.cart)
        self.assertEqual(cart_product.product, self.product)
        self.assertEqual(cart_product.quantity, 3)

    def test_create_cart_product_with_missing_cart(self):
        with self.assertRaises(IntegrityError):
            CartProducts.objects.create(product=self.product, quantity=3)

    def test_create_cart_product_with_missing_product(self):
        with self.assertRaises(IntegrityError):
            CartProducts.objects.create(cart=self.cart, quantity=3)

    def test_create_cart_product_with_quantity_as_string(self):
        with self.assertRaises(ValueError):
            CartProducts.objects.create(cart=self.cart, product=self.product, quantity='three')

    def test_create_cart_product_with_date_add(self):
        cart_product = CartProducts.objects.create(cart=self.cart, product=self.product, quantity=3, date_add=datetime.now())
        self.assertIsInstance(cart_product, CartProducts)
        self.assertNotEqual(cart_product.date_add, datetime.now())