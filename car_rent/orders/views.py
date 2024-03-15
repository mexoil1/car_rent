from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.viewsets import mixins

from .models import Order
from .serializers import OrderCreateSerializer, OrderListRetriveSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.select_related('car', 'renter')
    # permission_classes = {
    # }
    serializer_classes = {
        'create': OrderCreateSerializer,
        'list': OrderListRetriveSerializer,
        'retrive': OrderListRetriveSerializer,
    }
    permission_classes = {
        
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
    
    @action(detail=True, method=['Post'])
    def appruve(self, request, pk=None):

