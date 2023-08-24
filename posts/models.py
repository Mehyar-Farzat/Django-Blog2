from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=30000)
    publish_date = models.DateTimeField(default=timezone.now)
    

    

