# Generated by Django 4.1 on 2022-08-20 08:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('E_Comm_User', '0004_remove_user_address_remove_user_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mail',
            new_name='email',
        ),
    ]
