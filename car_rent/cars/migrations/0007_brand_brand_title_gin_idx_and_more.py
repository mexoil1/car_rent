# Generated by Django 5.0.2 on 2024-03-19 08:09

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_brand_options_alter_brandphoto_options_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            sql='CREATE EXTENSION IF NOT EXISTS pg_trgm;',
            reverse_sql='DROP EXTENSION IF EXISTS pg_trgm;'
        ),
        migrations.AddIndex(
            model_name='brand',
            index=django.contrib.postgres.indexes.GinIndex(
                fields=['title'], name='brand_title_gin_idx', opclasses=['gin_trgm_ops']),
        ),
        migrations.AddIndex(
            model_name='carmodel',
            index=django.contrib.postgres.indexes.GinIndex(
                fields=['title'], name='carmodel_title_gin_idx', opclasses=['gin_trgm_ops']),
        ),
    ]