# Generated by Django 4.2.1 on 2023-06-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_data', models.JSONField(default=dict)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
