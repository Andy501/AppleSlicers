# Generated by Django 4.1 on 2022-08-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slices', '0003_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='charges',
            field=models.FloatField(default=99.99),
        ),
        migrations.AlterField(
            model_name='payment',
            name='coupon',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.FloatField(default=0),
        ),
    ]
