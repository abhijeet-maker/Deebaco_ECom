# Generated by Django 4.1 on 2022-08-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('E_Comm_User', '0007_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('add', 'add'), ('update', 'update')], default='admin',
                                   max_length=20),
        ),
    ]
