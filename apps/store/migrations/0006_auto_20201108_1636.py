# Generated by Django 3.1.3 on 2020-11-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]