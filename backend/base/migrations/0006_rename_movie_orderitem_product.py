# Generated by Django 4.0.6 on 2022-07-28 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_movies__id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='movie',
            new_name='product',
        ),
    ]
