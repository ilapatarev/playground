# Generated by Django 4.2.3 on 2023-07-22 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='offer_field',
            new_name='offerer',
        ),
    ]
