# Generated by Django 3.1.3 on 2021-02-23 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_auto_20210219_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='spoon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spoons', to='store.spoon'),
        ),
    ]
