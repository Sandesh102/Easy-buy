# Generated by Django 5.1.4 on 2024-12-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='products/images/default.png', null=True, upload_to='products/images/'),
        ),
    ]
