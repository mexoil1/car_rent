from cars.models import Brand, CarModel
from rest_framework import serializers


class BrandBriefSerialzer(serializers.ModelSerializer):
    '''Brief serializer for brands'''
    class Meta:
        model = Brand
        fields = [
            'id',
            'title',
        ]


class CarModelBriefSerializer(serializers.ModelSerializer):
    '''Brief serializers for carmodels'''
    class Meta:
        model = CarModel
        fields = [
            'id',
            'title',
        ]
