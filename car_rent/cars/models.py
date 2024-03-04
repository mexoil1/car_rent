from core.models import BaseAbstractModel
from django.contrib.auth import get_user_model
from django.db import models

from .constants import Constants

User = get_user_model()


class Brand(models.Model):
    '''Model of car Brand'''
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(
        null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'Brand {self.title}'


class CarModel(models.Model):
    '''Model of car Template'''
    title = models.CharField(max_length=100, verbose_name='Название')
    type_of_fuel = models.CharField(
        max_length=10, choices=Constants.TYPES_OF_FUEL, verbose_name='Тип топлива')
    fuel_consumption = models.FloatField(verbose_name='Расход топлива')
    hp = models.IntegerField(verbose_name='Мощность')
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True, verbose_name='Марка')

    def __str__(self):
        return f'{self.title} - {self.hp} л.с.'


class Car(BaseAbstractModel):
    '''Model of User's Car'''
    car = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True)
    score = models.FloatField(default=5.0)
    price = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    langitude = models.FloatField()


class CarOptions(models.Model):
    '''Model of car option'''
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    option = models.CharField(max_length=200)


class CarModelPhoto(models.Model):
    '''Model of car model photo'''
    photo = models.ImageField()
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)


class BrandPhoto(models.Model):
    '''Model of brand photo'''
    photo = models.ImageField()
    car = models.ForeignKey(Brand, on_delete=models.CASCADE)


class CarPhoto(models.Model):
    '''Model of User's car photo'''
    photo = models.ImageField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
