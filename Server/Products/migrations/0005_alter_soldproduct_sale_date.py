# Generated by Django 4.2.5 on 2023-10-22 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_soldproduct_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldproduct',
            name='sale_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
