from rest_framework import generics
from .models import Cart, CartProducts
from .serializers import CartSerializer, CartCleanSerializer, CartProductsSerializer, CartProductDeleteSerializer
from .utils import SerializerByMethodMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from users.permissions import UpdateAndDelete


class CartCreateView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UpdateAndDelete]

    queryset = CartProducts.objects.all()
    serializer_map = {
        'GET': CartSerializer,
        'POST': CartProductsSerializer,
    }


class ProductCartRetrieveUpdateDestroyView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UpdateAndDelete]
    
    queryset = Cart.objects.all()
    serializer_map = {
        'GET': CartSerializer,
        'PATCH': CartCleanSerializer
    }


class CartProductDestroyView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UpdateAndDelete]
    
    queryset = Cart.objects.all()
    serializer_map = {
        'GET': CartProductDeleteSerializer,
        'PATCH': CartSerializer
    }
