# Generated by Django 3.1.3 on 2021-02-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20210208_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='instagram',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]