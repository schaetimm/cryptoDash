# Generated by Django 5.0.2 on 2024-03-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_broker_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker',
            name='image_url',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
    ]