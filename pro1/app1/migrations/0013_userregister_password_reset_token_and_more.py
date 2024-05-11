# Generated by Django 5.0.3 on 2024-05-04 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_userregister_is_verified_userregister_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='password_reset_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userregister',
            name='password_reset_token_expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
