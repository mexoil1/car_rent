# Generated by Django 5.0.2 on 2024-02-27 11:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(
                    blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='BrandPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('car', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='cars.brand')),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('type_of_fuel', models.CharField(choices=[(0, 'АИ-92'), (1, 'АИ-95'), (2, 'АИ-100'), (
                    3, 'ДТ'), (4, 'Газ'), (5, 'Электро')], max_length=10, verbose_name='Тип топлива')),
                ('fuel_consumption', models.FloatField(
                    verbose_name='Расход топлива')),
                ('hp', models.IntegerField(verbose_name='Мощность')),
                ('brand', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.brand', verbose_name='Марка')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=5.0)),
                ('price', models.IntegerField()),
                ('owner', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('car', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.carmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CarModelPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('car', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CarPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('car', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]
