# Generated by Django 5.0.1 on 2024-01-27 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='required_amount',
            field=models.PositiveBigIntegerField(default=100, help_text='required amount to use coupon'),
        ),
    ]
