# Generated by Django 5.1.1 on 2024-10-16 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_payment_slip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='slip',
        ),
    ]
