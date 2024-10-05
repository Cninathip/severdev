# Generated by Django 5.0.7 on 2024-10-05 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance', models.CharField(max_length=100)),
                ('price_per_hour', models.IntegerField()),
                ('price_per_day', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('description', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pay_at', models.DateTimeField(null=True)),
                ('pay_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.position')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vehicle_status', models.BooleanField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.detail')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.employee')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('return_status', models.BooleanField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.customer')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.payment')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.vehicle')),
            ],
        ),
    ]
