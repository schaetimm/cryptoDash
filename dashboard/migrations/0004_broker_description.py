# Generated by Django 5.0.2 on 2024-03-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_broker_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
