# Generated by Django 3.1.3 on 2020-11-20 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0003_auto_20201120_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping',
            old_name='is_valid',
            new_name='active',
        ),
    ]
