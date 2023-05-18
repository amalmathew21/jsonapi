from django.db import models

# Create your models here.

class MyModel(models.Model):
    json_file = models.JSONField(null=False, default=dict)
