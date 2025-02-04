# Generated by Django 5.1.2 on 2024-10-11 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_signal_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='middlename',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
