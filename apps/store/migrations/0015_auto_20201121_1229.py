# Generated by Django 3.1.3 on 2020-11-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20201121_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='flavour',
        ),
        migrations.AddField(
            model_name='flavour',
            name='product',
            field=models.ManyToManyField(related_name='flavours', to='store.Product'),
        ),
    ]