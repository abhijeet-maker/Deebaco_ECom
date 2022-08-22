# Generated by Django 4.1 on 2022-08-21 09:48

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('Inventory', '0005_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='pr_name'),
        ),
    ]
