from django.db import models
from django.contrib.postgres.fields import JSONField

class DataModel(models.Model):
    form_id = models.IntegerField(null=False)
    form_response = JSONField(null=False)