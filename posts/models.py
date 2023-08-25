from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author', on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=30000)
    publish_date = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts',null=True)
    


    def __str__(self):
        return self.title
    


