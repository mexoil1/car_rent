from cars.models import Brand, BrandPhoto, CarModel, CarModelPhoto
from rest_framework import serializers


class BrandPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandPhoto
        fields = ['photo',]


class BrandSerializer(serializers.ModelSerializer):
    '''Serializer of brands'''
    photos = BrandPhotoSerializer(source='brand_photo', many=True)

    class Meta:
        model = Brand
        fields = [
            'id',
            'title',
            'description',
            'photos',
        ]


class CarModelPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModelPhoto
        fields = ['photo',]


class CarModelSerializer(serializers.ModelSerializer):
    '''Serializer of car models'''
    photos = CarModelPhotoSerializer(source='carmodel_photo', many=True)
    brand = BrandSerializer()

    class Meta:
        model = CarModel
        fields = [
            'id',
            'title',
            'brand',
            'type_of_fuel',
            'fuel_consumption',
            'hp',
            'photos',
        ]
