from django.db import models

# Create your models here.

class MyModel(models.Model):
    json_file = models.JSONField(null=False, default=dict)

    def __str__(self):
        return f'MyModel object ({self.pk})'

class ImageModel(models.Model):
    json_data = models.JSONField(null=False, default=dict)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'MyModel object ({self.pk})'
