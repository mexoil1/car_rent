from core.models import BaseAbstractModel
from django.contrib.auth import get_user_model
from django.contrib.postgres.indexes import GinIndex
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Brand(models.Model):
    '''Model of car Brand'''
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(
        null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        indexes = [
            GinIndex(fields=['title',], name='brand_title_gin_idx',
                     opclasses=['gin_trgm_ops'])
        ]

    def __str__(self):
        return f'Brand {self.title}'


class CarModel(models.Model):
    '''Model of car Template'''
    class TYPES_OF_FUEL(models.TextChoices):
        '''Choices of fuel type'''
        AI_92 = '92', _('АИ-92')
        AI_95 = '95', _('АИ-95')
        AI_100 = '10', _('АИ-100')
        GAS = 'GS', _('Газ')
        DIESEL = 'DT', _('Дизельное топливо')
        ELECTRO = 'EL', _('Электричество')

    title = models.CharField(max_length=100, verbose_name='Название')
    type_of_fuel = models.CharField(
        max_length=10, choices=TYPES_OF_FUEL, verbose_name='Тип топлива', null=True)
    fuel_consumption = models.FloatField(verbose_name='Расход топлива')
    hp = models.IntegerField(verbose_name='Мощность')
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, null=True, verbose_name='Марка')

    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели'
        indexes = [
            GinIndex(fields=['title',], name='carmodel_title_gin_idx', opclasses=[
                     'gin_trgm_ops'])
        ]

    def __str__(self):
        return f'{self.title} - {self.hp} л.с.'


class Car(BaseAbstractModel):
    '''Model of User's Car'''
    car = models.ForeignKey(CarModel, on_delete=models.PROTECT, null=True)
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
    photo = models.ImageField(upload_to='car_models', verbose_name='Фото')
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE,
                            verbose_name='Модель машины', related_name='carmodel_photo')

    class Meta:
        verbose_name = 'Фотография модели машины'
        verbose_name_plural = 'Фотографии моделей машины'


class BrandPhoto(models.Model):
    '''Model of brand photo'''
    photo = models.ImageField(upload_to='brands', verbose_name='Фото')
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, verbose_name='Бренд', related_name='brand_photo')

    class Meta:
        verbose_name = 'Фотография бренда'
        verbose_name_plural = 'Фотографии бренда'


class CarPhoto(models.Model):
    '''Model of User's car photo'''
    photo = models.ImageField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
