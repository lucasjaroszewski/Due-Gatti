# Generated by Django 3.1.3 on 2021-02-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_product_spoon'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]