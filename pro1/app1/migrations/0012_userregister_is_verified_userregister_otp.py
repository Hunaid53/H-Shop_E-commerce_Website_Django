# Generated by Django 5.0.3 on 2024-04-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_order_address_order_email_order_name_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userregister',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
