# Generated by Django 4.2.9 on 2024-02-09 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buynow',
            name='payment_type',
            field=models.CharField(choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('paypal', 'PayPal')], max_length=20),
        ),
    ]
