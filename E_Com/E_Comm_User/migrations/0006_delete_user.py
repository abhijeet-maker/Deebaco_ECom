# Generated by Django 4.1 on 2022-08-20 09:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('E_Comm_User', '0005_rename_mail_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
