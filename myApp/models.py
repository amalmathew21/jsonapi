from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from django.contrib.postgres.fields import JSONField
from django.forms import DateInput

import json

json_data1 = '''
    [
      {
        "Display Name": "New",
        "Value": "LS1"
      },
      {
        "Display Name": "Assigned",
        "Value": "LS2"
      },
      {
        "Display Name": "In Process",
        "Value": "LS3"
      },
      {
        "Display Name": "Converted",
        "Value": "LS4"
      },
      {
        "Display Name": "Recycled",
        "Value": "LS5"
      },
      {
        "Display Name": "Dead",
        "Value": "LS6"
      }
    ]
    '''

choices_data = json.loads(json_data1)
dpLeadStatus = [(item['Value'], item['Display Name']) for item in choices_data]
for i in range(7, 51):
    dpLeadStatus.append((f'LS{i}', f'Choice {i}'))


# Create your models here.

class MyModel(models.Model):
    json_file = models.JSONField(null=False, default=dict)

    def __str__(self):
        return f'MyModel object ({self.pk})'


class DropdownModel(models.Model):
    json_data = models.JSONField(null=False, default=dict)
    def __str__(self):
        return f'DropdownModel object ({self.pk})'


class DataModel(models.Model):
    json_data = models.JSONField(null=False, default=dict)

    def __str__(self):
        return f'MyModel object ({self.pk})'


class Lead(models.Model):
    json_data = models.JSONField(default=dict)
    leadId = models.IntegerField(primary_key=True)
    firstName = models.TextField(null=True, blank=True)
    lastName = models.TextField(null=True, blank=True)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20, null=True, blank=True)
    fax = models.IntegerField(null=True, blank=True)
    company = models.TextField(null=True, blank=True)
    # dpLeadStatus = (
    #     ('LS1', 'New'),
    #     ('LS2', 'Assigned'),
    #     ('LS3', 'In Process'),
    #     ('LS4', 'Converted'),
    #     ('LS5', 'Recycled'),
    #     ('LS6', 'Dead')
    # )

    leadStatus = models.CharField(max_length=4, choices=dpLeadStatus, null=True, blank=True)
    dpLeadSource = (
        ('LSo1', 'Existing Customer'),
        ('LSo2', 'Self Generated'),
        ('LSo3', 'Employee'),
        ('LSo4', 'Converted'),
        ('LSo5', 'Partner'),
        ('LSo6', 'Public Relations'),
        ('LSo7', 'Other')
    )
    leadSource = models.CharField(max_length=4, choices=dpLeadSource, null=True, blank=True)

    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    createdDate = models.DateField(null=True, blank=True)
    modifiedDate = models.DateField(null=True, blank=True)
    accountName = models.TextField(null=True, blank=True)
    accountRevenue = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.json_data = {
            'leadId': self.leadId,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'phoneNumber': self.phoneNumber,
            'fax': self.fax,
            'company': self.company,
            'leadStatus': self.leadStatus,
            'leadSource': self.leadSource,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'pincode': self.pincode,
            # 'createdDate': self.createdDate,
            # 'modifiedDate': self.modifiedDate,
            'accountName': self.accountName,
            'accountRevenue': self.accountRevenue,
        }
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Lead {self.leadId}"

    class Meta:
        verbose_name_plural = 'Leads'

class Accounts(models.Model):
    json_data = models.JSONField(default=dict)
    accountId = models.IntegerField(primary_key=True)
    accountName = models.CharField(max_length=255)
    dpAccount_type = (
        ('AT1', 'Analyst'),
        ('AT2', 'Competitor'),
        ('AT3', 'Customer'),
        ('AT4', 'Investor'),
        ('AT5', 'Partner')
    )
    accountType = models.CharField(max_length=5, choices=dpAccount_type)
    accountNumber = models.BigIntegerField()
    dp_industry = (
        ('I1', 'Apparel'),
        ('I2', 'Banking'),
        ('I3', 'Environmental'),
        ('I4', 'Finance'),
        ('I5', 'Health Care'),
    )
    industry = models.CharField(max_length=5, choices=dp_industry)
    website = models.CharField(max_length=255)
    tickerSymbol = models.CharField(max_length=255)
    phoneNumber = models.BigIntegerField(unique=True, validators=[
        RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    billingAddress = models.CharField(max_length=255)
    shippingAddress = models.CharField(max_length=255)
    sicCode = models.BigIntegerField()
    createdDate = models.DateField(null=True, blank=True)
    modifiedDate = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.json_data = {
            'accountId': self.accountId,
            'accountName': self.accountName,
            'accountType': self.accountType,
            'accountNumber': self.accountNumber,
            'industry': self.industry,
            'website': self.fax,
            'tickerSymbol': self.tickerSymbol,
            'phoneNumber': self.phoneNumber,
            'billingAddress': self.billingAddress,
            'shippingAddress': self.shippingAddress,
            'sicCode': self.sicCode,
            # 'createdDate': self.createdDate,
            # 'modifiedDate': self.modifiedDate,
        }
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Account {self.accountId}"

    class Meta:
        verbose_name_plural = 'Accounts'

class Opportunities(models.Model):
    json_data = models.JSONField(default=dict)
    opportunityId = models.IntegerField(primary_key=True)
    opportunityName = models.CharField(max_length=255)
    dpOpportunityType = (
        ('EB1', 'Existing Business'),
        ('EB2', 'New Business')
    )
    opportunityType = models.CharField(max_length=10, choices=dpOpportunityType)
    accountId = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    leadId = models.ForeignKey(Lead, on_delete=models.CASCADE, null=True)
    dpLeadSource = (
        ('LSo1', 'Existing Customer'),
        ('LSo2', 'Self Generated'),
        ('LSo3', 'Employee'),
        ('LSo4', 'Converted'),
        ('LSo5', 'Partner'),
        ('LSo6', 'Public Relations'),
        ('LSo7', 'Other')
    )
    leadSource = models.CharField(max_length=5, choices=dpLeadSource)
    amount = models.FloatField()
    dpStage = (
        ('S1', 'Prospecting'),
        ('S2', 'Qualification'),
        ('S3', 'Needs Analysis'),
        ('S4', 'Value Proposition'),
        ('S5', 'Identify Decision Makers')

    )
    stage = models.CharField(max_length=10, choices=dpStage)
    expectedCloseDate = models.DateField()
    probability = models.CharField(max_length=255)
    createdDate = models.DateField(default=date.today)
    modifiedDate = models.DateField(default=date.today)

    def save(self, *args, **kwargs):
        self.json_data = {
            'opportunityId': self.opportunityId,
            'opportunityName': self.opportunityName,
            'opportunityType': self.opportunityType,
            'accountId': self.accountId,
            'leadId': self.leadId,
            'leadSource': self.leadSource,
            'amount': self.amount,
            'stage': self.stage,
            'expectedCloseDate': self.expectedCloseDate,
            'probability': self.probability,
            # 'createdDate': self.createdDate,
            # 'modifiedDate': self.modifiedDate,
        }
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Opportunity {self.opportunityId}"

    class Meta:
        verbose_name_plural = 'Oppurtunity'

class Task(models.Model):
    json_data = models.JSONField(default=dict)
    taskId = models.IntegerField(primary_key=True)
    taskName = models.TextField(blank=True)
    accountId = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    opportunityId= models.ForeignKey(Opportunities, on_delete=models.CASCADE, null=True)
    dueDate = models.DateField(null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    dpStatus = (
        ('ST1', 'Not Started'),
        ('ST2', 'In Progress'),
        ('ST3', 'Completed'),
        ('ST4', 'Pending Input'),
        ('ST5', 'Deferred'),
    )
    status = models.CharField(max_length=10, choices=dpStatus,null=True,blank=True)
    dpPriority = (
        ('P1', 'High'),
        ('P2', 'Medium'),
        ('P3', 'Low'),
    )
    priority = models.CharField(max_length=10, choices=dpPriority,null=True,blank=True)
    createdDate = models.DateField(null=True, blank=True)
    modifiedDate = models.DateField(null=True, blank=True)
    profilePic = models.ImageField(upload_to='task_profile_pics/', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.json_data = {
            'taskId': self.taskId,
            'taskName': self.taskName,
            'accountId': self.accountId,
            'opportunityId': self.opportunityId,
            # 'dueDate': self.dueDate,
            # 'startDate': self.startDate,
            'status': self.status,
            'priority': self.priority,
            # 'createdDate': self.createdDate,
            # 'modifiedDate': self.modifiedDate,
            #'profilePic':self.profilePic
        }
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Task {self.taskId}"

    class Meta:
        verbose_name_plural = 'Task'

class Report(models.Model):
    json_data = models.JSONField(default=dict)
    reportId = models.IntegerField()
    reportName = models.TextField(null=True, blank=True)
    accountId = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    opportunityId = models.ForeignKey(Opportunities, on_delete=models.CASCADE, null=True)
    createdDate = models.DateField(null=True, blank=True)
    modifiedDate = models.DateField(null=True, blank=True)


    def save(self, *args, **kwargs):
        self.json_data = {
            'reportId': self.taskId,
            'reportName': self.taskName,
            'accountId': self.accountId,
            'opportunityId': self.opportunityId,
            # 'createdDate': self.createdDate,
            # 'modifiedDate': self.modifiedDate,
        }
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Report {self.reportId}"

    class Meta:
        verbose_name_plural ='Report'

class Notes(models.Model):
    json_data = models.JSONField(default=dict)
    noteId = models.IntegerField()
    accountId = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    opportunityId = models.ForeignKey(Opportunities, on_delete=models.CASCADE, null=True)
    NOTE_CHOICES = (
        ('N1', 'note1'),
        ('N2', 'note2'),
        ('N3', 'note3'),
    )

    noteType = models.CharField(max_length=4, choices=NOTE_CHOICES)
    name = models.TextField(blank=True)
    profilePhoto = models.ImageField(upload_to='notes_profile_photos/',null=True, blank=True)

    def save(self, *args, **kwargs):
        self.json_data = {
            'noteId': self.noteId,
            'accountId': self.accountId,
            'opportunityId': self.opportunityId,
            'noteType': self.noteType,
            'name': self.name,
            #'profilePhoto':self.profilePhoto
        }
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Note {self.noteId}"

    class Meta:
        verbose_name_plural ='Note'