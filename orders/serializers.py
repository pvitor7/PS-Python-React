from rest_framework import serializers
from .models import Orders, OrderProducts
from products.models import Products
from django.forms.models import model_to_dict

class OrdersSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Orders
        fields = '__all__'
        
    def get_products(self, instance):
        order = Orders.objects.get(user=self.context['request'].user)
        list_products = []
        products = OrderProducts.objects.filter(order=order)
        for item in products:
            product_instance = Products.objects.get(id=item.product.id)
            dict_product = model_to_dict(product_instance)
            list_products.append(dict_product)
        return list_products
        
    