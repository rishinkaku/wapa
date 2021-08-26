# Generated by Django 3.2.6 on 2021-08-20 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_school_school_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='isat',
            name='date',
        ),
        migrations.RemoveField(
            model_name='isat',
            name='population',
        ),
        migrations.RemoveField(
            model_name='isat',
            name='school_id',
        ),
        migrations.RemoveField(
            model_name='isat',
            name='school_name',
        ),
        migrations.RemoveField(
            model_name='isat',
            name='subject_name',
        ),
        migrations.AddField(
            model_name='isat',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='isats', to='app.school'),
        ),
        migrations.AddField(
            model_name='isat',
            name='subject',
            field=models.IntegerField(choices=[(10, 'English'), (20, 'Math'), (30, 'Science')], null=True),
        ),
        migrations.AlterField(
            model_name='isat',
            name='grade',
            field=models.IntegerField(choices=[(1, 'All'), (3, 'Third'), (4, 'Fourth Grade'), (5, 'Fifth Grade'), (6, 'Sixth Grade'), (7, 'Seventh Grade'), (8, 'Eighth Grade'), (10, 'High School')], null=True),
        ),
    ]