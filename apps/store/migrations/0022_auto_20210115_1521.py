# Generated by Django 3.1.3 on 2021-01-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20210115_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sabores',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
