# Generated by Django 5.1.3 on 2024-12-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
