from rest_framework import serializers
from .models import Cart, CartProducts
from products.models import Products
from django.forms.models import model_to_dict
from orders.models import OrderProducts, Orders


class CartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    products = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products',
                  'createdAt', 'updatedAt',  'is_finished']

    def get_products(self, instance):
        cart = Cart.objects.get(user=self.context['request'].user)
        list_products = []
        products = CartProducts.objects.filter(cart=cart)
        for item in products:
            product_instance = Products.objects.get(id=item.product.id)
            dict_product = model_to_dict(product_instance)
            list_products.append(dict_product)
        return list_products

    def get_extra_kwargs(self):
        if self.context['request'].data.get('product_id'):
            product = Products.objects.get(id=self.context['request'].data['product_id'])
            CartProducts.objects.filter(product=product).delete()
        return super().get_extra_kwargs()


class CartCleanSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = ['id', 'user',
                  'createdAt', 'updatedAt',  'is_finished']

    def get_extra_kwargs(self):
        if self.context['request'].data['is_finished']:
            
            new_order = Orders.objects.create(user=self.context['request'].user);
            cart = Cart.objects.get(user=self.context['request'].user)
            producs_cart = CartProducts.objects.filter(cart=cart)
            quantity_products = 0
            delivery = 0
            subtotal = 0
            
            for item in producs_cart:
                OrderProducts.objects.create(product=item.product, quantity=item.quantity, order=new_order)
                subtotal = subtotal + Products.objects.get(id=item.product.id).price
                delivery = delivery + (10 * item.quantity)
                quantity_products = quantity_products + item.quantity
            
            if delivery < 250:
                Orders.objects.filter(id=new_order.id).update(delivery=delivery, total=subtotal+delivery);
            else:
                Orders.objects.filter(id=new_order.id).update(total=subtotal);
                
            Orders.objects.filter(id=new_order.id).update(subtotal=subtotal);
            CartProducts.objects.filter(cart=cart).delete()
        return super().get_extra_kwargs()


class CartProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProducts
        fields = ['cart', 'product', 'quantity']

    def get_extra_kwargs(self):
        cart = Cart.objects.get(user=self.context['request'].user)
        product = Products.objects.get(
            id=self.context['request'].data['product_id'])
        list_cart_product = CartProducts.objects.filter(
            cart=cart, product=product)

        if len(list_cart_product) > 0:
            CartProducts.objects.filter(product=product).delete()
            self.context['request'].data['quantity'] = self.context['request'].data['quantity']

        self.context['request'].data['cart'] = cart.id
        self.context['request'].data['product'] = product.id
        return super().get_extra_kwargs()



class CartProductDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProducts
        fields = ['id', 'cart', 'product', 'quantity']
        