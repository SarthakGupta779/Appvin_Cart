# Generated by Django 4.2.9 on 2024-02-09 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
