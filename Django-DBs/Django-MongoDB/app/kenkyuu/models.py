from django.db import models
from djongo import models
from djongo.models import JSONField


class DataModel(models.Model):
    form_id = models.IntegerField(null=False)
    form_response = JSONField(null=False)
