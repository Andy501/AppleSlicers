# Generated by Django 4.1 on 2022-08-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slices', '0007_payment_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='last_payment_date',
            field=models.DateField(blank=True, default='2001-1-1'),
            preserve_default=False,
        ),
    ]