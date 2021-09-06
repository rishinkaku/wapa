# Generated by Django 3.2.7 on 2021-09-06 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_alter_account_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='account', to='app.zone'),
        ),
    ]