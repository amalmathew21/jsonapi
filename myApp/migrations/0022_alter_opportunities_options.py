# Generated by Django 4.2.1 on 2023-06-16 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0021_alter_opportunities_json_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opportunities',
            options={'verbose_name_plural': 'Opportunity'},
        ),
    ]
