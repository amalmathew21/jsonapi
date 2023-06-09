from django.db import models
from django.core.validators import RegexValidator
from datetime import date

# Create your models here.

class MyModel(models.Model):
    json_file = models.JSONField(null=False, default=dict)

    def __str__(self):
        return f'MyModel object ({self.pk})'

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'MyModel object ({self.pk})'


class DataModel(models.Model):
    json_data = models.JSONField(null=False, default=dict)
    def __str__(self):
        return f'MyModel object ({self.pk})'



class Leads(models.Model):
    leadId = models.IntegerField(primary_key = True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = models.BigIntegerField(unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    fax = models.BigIntegerField()
    company = models.CharField(max_length=255)
    dpLeadStatus = (
        ('LS1', 'New'),
        ('LS2', 'Assigned'),
        ('LS3', 'In Process'),
        ('LS4', 'Converted'),
        ('LS5', 'Recycled'),
        ('LS6', 'Dead')
    )
    leadStatus = models.CharField(max_length=4, choices=dpLeadStatus)
    dpLeadSource = (
        ('LSo1', 'Existing Customer'),
        ('LSo2', 'Self Generated'),
        ('LSo3', 'Employee'),
        ('LSo4', 'Converted'),
        ('LSo5', 'Partner'),
        ('LSo6', 'Public Relations'),
        ('LSo7', 'Other')
    )
    leadSource = models.CharField(max_length=4, choices=dpLeadSource)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.BigIntegerField()
    createdDate = models.DateField(default=date.today)
    modifiedDate = models.DateField(default=date.today)
    accountName = models.CharField(max_length=255)
    accountRevenue = models.BigIntegerField()

    def __str__(self):
        return str(self.leadId)

    class Meta:
        verbose_name_plural = 'Leads'





