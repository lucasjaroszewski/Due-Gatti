# Generated by Django 3.1.3 on 2021-02-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_auto_20210218_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='spoon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]