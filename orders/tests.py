from django.test import TestCase
from .models import User, Products, Orders, OrderProducts
import uuid

class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = User.objects.create(username='testuser', email='testuser@test.com', cellphone='1234567890')
        cls.product = Products.objects.create(name='testproduct', price=9.99, score=4, image='testimage')
        cls.order = Orders.objects.create(user=cls.user, subtotal=9.99, delivery=1.99, total=11.98)
        cls.orderproduct = OrderProducts.objects.create(order=cls.order, product=cls.product, quantity=1)

    def test_orders_user_foreign_key(self):
        order = Orders.objects.get(id=self.order.id)
        self.assertEqual(order.user, self.user)

    # def test_orders_subtotal_default_value(self):
    #     order = Orders.objects.get(id=self.order.id)
    #     self.assertEqual(order.subtotal, 0)

    # def test_orders_delivery_default_value(self):
    #     order = Orders.objects.get(id=self.order.id)
    #     self.assertEqual(order.delivery, 0)

    # def test_orders_total_default_value(self):
    #     order = Orders.objects.get(id=self.order.id)
    #     self.assertEqual(order.total, 0)

    def test_orders_createdAt(self):
        order = Orders.objects.get(id=self.order.id)
        self.assertIsNotNone(order.created_at)

    def test_orderproducts_order_foreign_key(self):
        orderproduct = OrderProducts.objects.get(id=self.orderproduct.id)
        self.assertEqual(orderproduct.order, self.order)

    def test_orderproducts_product_foreign_key(self):
        orderproduct = OrderProducts.objects.get(id=self.orderproduct.id)
        self.assertEqual(orderproduct.product, self.product)

    def test_orderproducts_quantity(self):
        orderproduct = OrderProducts.objects.get(id=self.orderproduct.id)
        self.assertEqual(orderproduct.quantity, 1)

    def test_orderproducts_id_is_uuid(self):
        orderproduct = OrderProducts.objects.get(id=self.orderproduct.id)
        self.assertIsInstance(orderproduct.id, uuid.UUID)

    def test_orders_id_is_uuid(self):
        order = Orders.objects.get(id=self.order.id)
        self.assertIsInstance(order.id, uuid.UUID)

    def test_user_id_is_uuid(self):
        user = User.objects.get(id=self.user.id)
        self.assertIsInstance(user.id, uuid.UUID)