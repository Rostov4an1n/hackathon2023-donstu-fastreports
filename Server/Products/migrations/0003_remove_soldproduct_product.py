# Generated by Django 4.2.5 on 2023-10-22 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_remove_soldproduct_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soldproduct',
            name='product',
        ),
    ]
