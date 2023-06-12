# Generated by Django 4.2.1 on 2023-06-12 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_leads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leads',
            name='leadSource',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='leadStatus',
        ),
        migrations.CreateModel(
            name='LeadsDropDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leadStatus', models.CharField(choices=[('LS1', 'New'), ('LS2', 'Assigned'), ('LS3', 'In Process'), ('LS4', 'Converted'), ('LS5', 'Recycled'), ('LS6', 'Dead')], max_length=4)),
                ('leadSource', models.CharField(choices=[('LSo1', 'Existing Customer'), ('LSo2', 'Self Generated'), ('LSo3', 'Employee'), ('LSo4', 'Converted'), ('LSo5', 'Partner'), ('LSo6', 'Public Relations'), ('LSo7', 'Other')], max_length=4)),
                ('leadId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.leads')),
            ],
        ),
    ]
