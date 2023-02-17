from django.test import TestCase
from .models import Products


class ProductsModelTest(TestCase):
    def setUp(self):
        self.product = {
            "name": "The Witcher III Wild Hunt",
            "price": 119.5,
            "score": 250,
            "image": "the-witcher-iii-wild-hunt.png",
        }

    def test_create_product_with_valid_data(self):
        new_product = Products.objects.create(**self.product)
        self.assertEqual(new_product.name, self.product["name"])
        self.assertEqual(new_product.price, self.product["price"])
        self.assertEqual(new_product.score, self.product["score"])
        self.assertEqual(new_product.image, self.product["image"])

    def test_name_field(self):
        name = Products._meta.get_field("name")
        self.assertEquals(name.max_length, 100)
        self.assertFalse(name.null)
        self.assertFalse(name.blank)

    def test_price_field(self):
        price = Products._meta.get_field("price")
        self.assertFalse(price.null)
        self.assertFalse(price.blank)

    def test_score_field(self):
        score = Products._meta.get_field("score")
        self.assertFalse(score.null)
        self.assertFalse(score.blank)

    def test_image_field(self):
        image = Products._meta.get_field("image")
        self.assertEquals(image.max_length, 100)
        self.assertFalse(image.null)
        self.assertFalse(image.blank)
