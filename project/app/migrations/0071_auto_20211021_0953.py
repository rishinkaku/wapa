# Generated by Django 3.2.8 on 2021-10-21 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0070_account_is_out'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ('-created',)},
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_out',
        ),
        migrations.RemoveField(
            model_name='account',
            name='story',
        ),
    ]