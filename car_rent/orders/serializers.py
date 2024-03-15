from  rest_framework import serializers

from .models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['car', 'renter', 'desired_date', ]


class OrderListRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['car', 'renter', 'desired_date', 'status',
                  'start_rent_time', ]
# TODO После появления дизайна возможно, нужно будет добавить
# отдельный сериализатор для ретрива
