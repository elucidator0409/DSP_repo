# Generated by Django 4.0.6 on 2022-07-19 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='PaymentMethod',
            new_name='paymentMethod',
        ),
    ]
