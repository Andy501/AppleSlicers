# Generated by Django 4.1 on 2022-08-24 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slices', '0004_alter_payment_charges_alter_payment_coupon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='id',
        ),
        migrations.AlterField(
            model_name='payment',
            name='coupon',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
