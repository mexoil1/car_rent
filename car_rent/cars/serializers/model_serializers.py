from cars.models import Brand
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    '''Serializer of brands'''
    class Meta:
        model = Brand
        fields = [
            'id',
            'title',
            'description',
        ]
