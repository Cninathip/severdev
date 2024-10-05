# Generated by Django 5.0.7 on 2024-10-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='image_url',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vehicles/'),
        ),
        migrations.AddField(
            model_name='vehicletype',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='type/'),
        ),
    ]
