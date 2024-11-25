from django.utils import timezone
import uuid
from django.db import models

class RecipeModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, unique=True, null=True)
    making_time = models.CharField(max_length=50, null=True)
    serves = models.CharField(max_length=50, null=True)
    ingredients = models.CharField(max_length=50, null=True)
    cost = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)