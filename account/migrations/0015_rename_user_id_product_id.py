# Generated by Django 4.2.9 on 2024-02-10 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_buynow_payment_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user_id',
            new_name='id',
        ),
    ]