# Generated by Django 5.0.2 on 2024-03-05 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_created_at_car_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brandphoto',
            old_name='car',
            new_name='brand',
        ),
        migrations.AlterField(
            model_name='brandphoto',
            name='photo',
            field=models.ImageField(upload_to='brands'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.carmodel'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.brand', verbose_name='Марка'),
        ),
    ]
