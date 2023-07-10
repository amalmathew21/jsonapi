from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from django.contrib.postgres.fields import JSONField
from django.forms import DateInput
from django.core.serializers.json import DjangoJSONEncoder
from django.core.files.storage import default_storage
from django.apps import apps
import json
import os
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import uuid
import imghdr
import random
import string
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

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


def save_base64_image(self, data, file_path):
    image_data = base64.b64decode(data)
    image_file = ContentFile(image_data, name=file_path)
    default_storage.save(file_path, image_file)


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
    annualRevenue = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.leadId)

    class Meta:
        verbose_name_plural = 'Leads'


class Accounts(models.Model):
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

    def __str__(self):
        return str(self.accountId)

    class Meta:
        verbose_name_plural = 'Accounts'





class Opportunities(models.Model):
    opportunityId = models.IntegerField(primary_key=True)
    opportunityName = models.TextField(null=True, blank=True)
    dpOpportunityType = (
        ('OT1', 'Type 1'),
        ('OT2', 'Type 2'),
        ('OT3', 'Type 3'),
    )
    opportunityType = models.CharField(max_length=3, choices=dpOpportunityType, null=True, blank=True)
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
    leadSource = models.CharField(max_length=4, choices=dpLeadSource, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    dpStage = (
        ('S1', 'Stage 1'),
        ('S2', 'Stage 2'),
        ('S3', 'Stage 3'),
        ('S4', 'Stage 4'),
        ('S5', 'Stage 5'),
    )
    stage = models.CharField(max_length=2, choices=dpStage, null=True, blank=True)
    expectedCloseDate = models.DateField(null=True, blank=True)
    probability = models.IntegerField(null=True, blank=True)
    createdDate = models.DateField(null=True, blank=True)
    modifiedDate = models.DateField(null=True, blank=True)
    profilePhoto = models.ImageField(upload_to='opportunity_photos/', null=True, blank=True)

    # def save_base64_image(self, data, file_path):
    #     image_data = base64.b64decode(data)
    #     image_file = ContentFile(image_data, name=file_path)
    #     default_storage.save(file_path, image_file)

    @staticmethod
    def save_base64_image(base64_string, file_name):
        try:
            image_data = base64.b64decode(base64_string)
            image = Image.open(BytesIO(image_data))
            image.save(file_name)
            return True

        except Exception as e:
            print(f"Error saving image: {str(e)}")
            return False
    def save(self, *args, **kwargs):
        if self.profilePhoto:
            if isinstance(self.profilePhoto, str):
                image_format = imghdr.what(None, h=self.profilePhoto)
                file_extension = image_format if image_format else 'jpg'
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                file_name = f'opportunity_photos/{self.opportunityId}_{random_string}.{file_extension}'
                self.save_base64_image(self.profilePhoto, file_name)
                self.profilePhoto = file_name

            elif isinstance(self.profilePhoto, InMemoryUploadedFile):
                image_format = imghdr.what(None, h=self.profilePhoto.read())
                file_extension = image_format if image_format else 'jpg'
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                file_name = f'opportunity_photos/{self.opportunityId}_{random_string}.{file_extension}'
                file_content = ContentFile(self.profilePhoto.read())
                default_storage.save(file_name, file_content)
                self.profilePhoto = file_name

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.opportunityId)

    class Meta:
        verbose_name_plural = 'Opportunities'


class Task(models.Model):
    taskId = models.IntegerField(primary_key=True)
    taskName = models.TextField(blank=True)
    accountId = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    opportunityId = models.ForeignKey(Opportunities, on_delete=models.CASCADE, null=True)
    dueDate = models.DateField(null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    dpStatus = (
        ('ST1', 'Not Started'),
        ('ST2', 'In Progress'),
        ('ST3', 'Completed'),
        ('ST4', 'Pending Input'),
        ('ST5', 'Deferred'),
    )
    status = models.CharField(max_length=10, choices=dpStatus, null=True, blank=True)
    dpPriority = (
        ('P1', 'High'),
        ('P2', 'Medium'),
        ('P3', 'Low'),
    )
    priority = models.CharField(max_length=10, choices=dpPriority, null=True, blank=True)
    createdDate = models.DateField(null=True, blank=True)
    modifiedDate = models.DateField(null=True, blank=True)
    profilePic = models.ImageField(upload_to='task_profile_pics/', null=True, blank=True)

    def save_base64_image(self, data, file_path):
        image_data = base64.b64decode(data)
        image_file = ContentFile(image_data, name=file_path)
        default_storage.save(file_path, image_file)

    def save(self, *args, **kwargs):
        if self.profilePic:
            if isinstance(self.profilePic, str):
                image_format = imghdr.what(self.profilePic)
                file_extension = image_format if image_format else 'jpg'
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                file_name = f'task_profile_pics/{self.taskId}_{random_string}.{file_extension}'
                self.save_base64_image(self.profilePic, file_name)
                self.profilePic = file_name

            else:
                image_format = imghdr.what(self.profilePic)
                file_extension = image_format if image_format else 'jpg'
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                file_name = f'task_profile_pics/{self.taskId}_{random_string}.{file_extension}'
                default_storage.save(file_name, self.profilePic)
                self.profilePic = file_name

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.taskId)

    class Meta:
        verbose_name_plural = 'Task'


class Report(models.Model):
    reportId = models.IntegerField(primary_key=True)
    reportName = models.TextField(null=True, blank=True)
    accountId = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    opportunityId = models.ForeignKey(Opportunities, on_delete=models.CASCADE, null=True)
    createdDate = models.DateField(null=True, blank=True)
    modifiedDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.reportId)

    class Meta:
        verbose_name_plural = 'Report'


class Notes(models.Model):
    noteId = models.IntegerField(primary_key=True)
    accountId = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    opportunityId = models.ForeignKey(Opportunities, on_delete=models.CASCADE, null=True)
    NOTE_CHOICES = (
        ('N1', 'note1'),
        ('N2', 'note2'),
        ('N3', 'note3'),
        ('N4', 'note4')
    )

    noteType = models.CharField(max_length=4, choices=NOTE_CHOICES)
    name = models.TextField(blank=True)
    profilePhoto = models.ImageField(upload_to='notes_profile_photos/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.profilePhoto:
            if isinstance(self.profilePhoto, str):
                # Handle base64-encoded image data
                file_extension = 'jpg'  # Specify the file extension based on the actual image format
                file_name = f'notes_profile_photos/{self.name}.{file_extension}'
                save_base64_image(self.profilePhoto, file_name)
                self.profilePhoto = file_name
            else:
                # Handle uploaded file
                file_name, file_extension = os.path.splitext(self.profilePhoto.name)
                file_extension = file_extension.lstrip('.')  # Remove the dot from the file extension
                file_name = f'notes_profile_photos/{self.name}.{file_extension}'
                default_storage.save(file_name, self.profilePhoto)
                self.profilePhoto = file_name
        else:
            self.profilePhoto = None

        super().save(*args, **kwargs)

        def __str__(self):
            return str(self.noteId)

    class Meta:
        verbose_name_plural = 'Note'









# from django.db import models
# from django.apps import apps


# class OrdoReports(models.Model):
#     ordoreportid = models.IntegerField(primary_key=True)
#     assignedTo = models.TextField(default="admin")
#     chart_choices = [
#         ('line', 'line'),
#         ('bar', 'bar'),
#         ('doughnut', 'doughnut'),
#         ('pie', 'pie'),
#     ]
#     chart = models.CharField(max_length=10, choices=chart_choices, blank=True)
#     description = models.TextField(blank=True)
#     name = models.CharField(max_length=255, blank=False)
#     fieldName_choices = [
#         ('Lead', 'Lead'),
#         ('Accounts', 'Accounts'),
#         ('Opportunities', 'Opportunities'),
#         ('Task', 'Task'),
#     ]
#     fieldName = models.CharField(max_length=255, choices=fieldName_choices, null=True, blank=False)
#     fieldLabel = models.CharField(max_length=255, blank=True)
#     sort_choices = [
#         ('asc', 'Ascending'),
#         ('desc', 'Descending'),
#     ]
#     sortBy = models.CharField(max_length=4, choices=sort_choices, null=False, blank=False)
#
#     def __str__(self):
#         return self.description
#
#     def save(self, *args, **kwargs):
#         if self.fieldName:
#             model = apps.get_model(app_label='myApp', model_name=self.fieldName)
#             if model:
#                 field_names = [field.name for field in model._meta.get_fields() if isinstance(field, models.Field)]
#                 self.fieldLabel = ', '.join(field_names)
#             else:
#                 self.fieldLabel = ''
#
#         super().save(*args, **kwargs)



# class OrdoReports(models.Model):
#     CHART_CHOICES = (
#         ('line', 'Line'),
#         ('bar', 'Bar'),
#         ('doughnut', 'Doughnut'),
#         ('pie', 'Pie'),
#     )
#
#     SORT_CHOICES = (
#         ('asc', 'Ascending'),
#         ('desc', 'Descending'),
#     )
#     ordoreportid = models.IntegerField(primary_key=True)
#     assignedTo = models.CharField(max_length=50, default='admin')
#     chartType = models.CharField(max_length=50, choices=CHART_CHOICES)
#     description = models.TextField()
#     groupByField = models.CharField(max_length=50, choices=[])
#     groupByLabel = models.CharField(max_length=50, choices=[], null=True, blank=True)
#     name = models.CharField(max_length=50)
#     primaryModule = models.CharField(max_length=50, choices=[])
#     summaryField = models.CharField(max_length=50, choices=[])
#     summaryLabel = models.CharField(max_length=50, choices=[], null=True, blank=True)
#     sortBy = models.CharField(max_length=50, choices=SORT_CHOICES)
#
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#
#         module_fields = {
#             'Lead': ['leadId', 'firstName','lastName', 'email','phoneNumber', 'fax','company', 'leadStatus','leadSource', 'city','state', 'country','pincode', 'createdDate','modifiedDate', 'accountName','annualRevenue'],
#             'Accounts': ['accountId', 'accountName','accountType', 'accountNumber','industry', 'website','tickerSymbol', 'phoneNumber','billingAddress', 'shippingAddress','sicCode', 'createdDate','modifiedDate'],
#             'Opportunities': ['opportunityId', 'opportunityName','opportunityType', 'accountId','leadId', 'leadSource','amount', 'stage','expectedCloseDate', 'probability', 'createdDate','modifiedDate','profilePhoto'],
#             'Task': ['taskId', 'taskName','accountType', 'accountId','opportunityId', 'dueDate','startDate', 'status','priority', 'createdDate','modifiedDate','profilePic'],
#         }
#
#         self._meta.get_field('groupByField').choices = [(field, field) for field in
#                                                         module_fields.get(self.primaryModule, [])]
#         self._meta.get_field('summaryField').choices = [(field, field) for field in
#                                                         module_fields.get(self.primaryModule, [])]
#         self._meta.get_field('primaryModule').choices = [(module, module) for module in module_fields.keys()]
#         self._meta.get_field('groupByLabel').choices = self._meta.get_field('groupByField').choices
#         self._meta.get_field('summaryLabel').choices = self._meta.get_field('summaryField').choices
#
#
#         self.groupByLabel = self.groupByField
#         self.summaryLabel = self.summaryField
#         super().save(*args, **kwargs)




class Ordo_Report(models.Model):
    CHART_CHOICES = (
        ('line', 'Line'),
        ('bar', 'Bar'),
        ('doughnut', 'Doughnut'),
        ('pie', 'Pie'),
    )

    SORT_CHOICES = (
        ('ASC', 'Ascending'),
        ('DSC', 'Descending'),
    )
    SORTBY_CHOICES = (
        ('createdDate','createdDate'),
        ('modifiedDate','modifiedDate'),
    )


    assignedTo = models.CharField(max_length=50, default='admin')
    chartType = models.CharField(max_length=50, choices=CHART_CHOICES)
    description = models.TextField()
    fields = models.JSONField(default=list)  # New field for storing the "fields" attribute
    groupByField = models.CharField(max_length=50)
    groupByLabel = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    primaryModule = models.CharField(max_length=50)
    summaryField = models.CharField(max_length=50)
    summaryLabel = models.CharField(max_length=50)
    sortBy = models.CharField(max_length=50, choices=SORTBY_CHOICES)
    sortOrder = models.CharField(max_length=50,choices=SORT_CHOICES)

    def __str__(self):
        return self.name + str(self.id)

    @classmethod
    def create_from_raw_data(cls, data):
        primary_module = data.get("primaryModule")
        model = apps.get_model(app_label='your_app_label', model_name=primary_module)

        fields_data = data.get("fields", [])
        fields = []
        for field_data in fields_data:
            field_name = field_data.get("fieldName")
            field_label = field_data.get("fieldLabel")
            if field_name in model._meta.get_all_field_names():
                fields.append({"fieldName": field_name, "fieldLabel": field_label})

        created_date_values = [getattr(instance, "createdDate") for instance in model.objects.all()]
        modified_date_values = [getattr(instance, "modifiedDate") for instance in model.objects.all()]


        if "createdDate" in data.get("sortBy", ""):
            data["sortBy"] = created_date_values
        elif "modifiedDate" in data.get("sortBy", ""):
            data["sortBy"] = modified_date_values

        return cls(
            assignedTo=data.get("assignedTo"),
            chartType=data.get("chartType"),
            description=data.get("description"),
            fields=fields,
            groupByField=data.get("groupByField"),
            groupByLabel=data.get("groupByLabel"),
            name=data.get("name"),
            primaryModule=data.get("primaryModule"),
            summaryField=data.get("summaryField"),
            summaryLabel=data.get("summaryLabel"),
            sortBy=data.get("sortBy"),
            sortOrder=data.get("sortOrder"),
        )

    def save(self, *args, **kwargs):
        self.groupByLabel = self.groupByField
        self.summaryLabel = self.summaryField
        super().save(*args, **kwargs)


