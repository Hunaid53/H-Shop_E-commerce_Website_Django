# Generated by Django 4.2.4 on 2023-08-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='productprice',
            field=models.CharField(default='', max_length=200),
        ),
    ]