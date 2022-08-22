# Generated by Django 4.1 on 2022-08-21 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=200)),
                ('size_length', models.IntegerField(default=0)),
                ('size_UK', models.IntegerField(default=0)),
                ('size_US', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_name', models.CharField(max_length=200)),
                ('act_price', models.CharField(max_length=200)),
                ('disc_price', models.IntegerField(default=0)),
                ('pr_fabric', models.CharField(max_length=200)),
                ('pr_colour', models.CharField(max_length=200)),
                ('pr_discription', models.TextField(default=None)),
                ('pr_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.size')),
            ],
        ),
    ]