from cars.models import Brand
from rest_framework import serializers


class BrandBriefSerialzer(serializers.ModelSerializer):
    '''Brief serializer of brands'''
    class Meta:
        model = Brand
        fields = [
            'id',
            'title',
        ]
