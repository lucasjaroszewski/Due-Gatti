# Generated by Django 3.1.3 on 2021-02-08 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20210116_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='flavor',
        ),
    ]
