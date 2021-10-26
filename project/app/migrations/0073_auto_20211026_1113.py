# Generated by Django 3.2.8 on 2021-10-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0072_alter_account_is_precise'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='nurse_email',
            field=models.EmailField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='school',
            name='nurse_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='exemption',
            field=models.ImageField(blank=True, default='wapa/exemption', null=True, upload_to=''),
        ),
    ]
