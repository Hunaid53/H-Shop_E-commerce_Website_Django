# Generated by Django 4.2.4 on 2023-08-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_vendorregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendorid',
            field=models.CharField(default='', max_length=200),
        ),
    ]
