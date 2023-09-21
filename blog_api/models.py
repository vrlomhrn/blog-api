from django.db import models
from datetime import datetime

from django.contrib.auth import get_user
import uuid


# Create models here
    
class Blog(models.Model):
    blog_id = models.UUIDField(unique=True, default=uuid.uuid4(), primary_key=True, editable=False, auto_created=True)
    title = models.CharField(max_length=140)
    slug = models.SlugField(default=f'{title}'.lower(), unique=True, auto_created=True)
    description = models.TextField()
    created_at = models.DateField(default=datetime.now())
    updated_at = models.DateField(default=datetime.now())
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    category_id = models.UUIDField(unique=True, default=uuid.uuid4(), primary_key=True, editable=False, auto_created=True)
    blogs = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category_title = models.CharField(max_length=55)
    created_at = models.DateField(default=datetime.now())
    updated_at = models.DateField(default=datetime.now())
    
    def __str__(self):
        return self.category_title
    
    
class Comment(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    posted_at = models.DateField(default=datetime.now())