# Generated by Django 3.1.3 on 2021-01-16 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_orderitem_sabores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='sabores',
            new_name='flavor',
        ),
    ]
