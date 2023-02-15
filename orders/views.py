from rest_framework import generics
from .serializers import OrdersSerializer
from .models import Orders

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from users.permissions import UpdateAndDelete

class OrderListCreate(generics.ListAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UpdateAndDelete]
    
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class OrderRetrieveUpdateDestroy(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UpdateAndDelete]
    
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer