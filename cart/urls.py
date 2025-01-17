from django.urls import path
from .views import CartCreateView, ProductCartRetrieveUpdateDestroyView, CartProductDestroyView

urlpatterns = [
path('', CartCreateView.as_view(), name='cart-list-create'),

path('<pk>/', ProductCartRetrieveUpdateDestroyView.as_view(), name='cart-retrieve-update-delete'),

path('products/<pk>/', CartProductDestroyView.as_view(), name='cart-list-create'),
]