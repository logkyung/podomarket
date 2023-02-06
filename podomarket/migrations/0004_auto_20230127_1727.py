# Generated by Django 2.2 on 2023-01-27 17:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0003_auto_20230127_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='item_condition',
            field=models.CharField(choices=[('새제품', '새제품'), ('최상', '최상'), ('상', '상'), ('중', '중'), ('하', '하')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='item_price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]