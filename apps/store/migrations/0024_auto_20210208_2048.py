# Generated by Django 3.1.3 on 2021-02-08 20:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cat',
            options={'ordering': ('-date_added',)},
        ),
        migrations.RemoveField(
            model_name='cat',
            name='owner',
        ),
        migrations.AddField(
            model_name='cat',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
