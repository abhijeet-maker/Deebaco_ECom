# Generated by Django 4.1 on 2022-08-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('E_Comm_User', '0003_user_role_alter_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='abhijeet', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('add', 'add'), ('update', 'update')], default=1,
                                   max_length=20),
        ),
    ]
