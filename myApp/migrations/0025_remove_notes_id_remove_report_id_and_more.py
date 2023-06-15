# Generated by Django 4.2.1 on 2023-06-16 06:43

from django.db import migrations, models
import myApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0024_alter_opportunities_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='id',
        ),
        migrations.RemoveField(
            model_name='report',
            name='id',
        ),
        migrations.AlterField(
            model_name='notes',
            name='json_data',
            field=models.JSONField(default=dict, encoder=myApp.models.CustomJSONEncoder),
        ),
        migrations.AlterField(
            model_name='notes',
            name='noteId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='notes',
            name='noteType',
            field=models.CharField(choices=[('N1', 'note1'), ('N2', 'note2'), ('N3', 'note3'), ('N4', 'note4')], max_length=4),
        ),
        migrations.AlterField(
            model_name='report',
            name='json_data',
            field=models.JSONField(default=dict, encoder=myApp.models.CustomJSONEncoder),
        ),
        migrations.AlterField(
            model_name='report',
            name='reportId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='json_data',
            field=models.JSONField(default=dict, encoder=myApp.models.CustomJSONEncoder),
        ),
    ]
