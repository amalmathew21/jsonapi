# Generated by Django 4.2.1 on 2023-06-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_remove_leads_json_data_remove_leads_leadstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='json_data',
            field=models.JSONField(default=dict),
        ),
    ]
