from django.db import models
from datetime import datetime
import uuid


# Create models here
class Blog(models.Model):
    blog_id = models.UUIDField(
        unique=True, default=uuid.uuid4(), primary_key=True, editable=False
    )
    title = models.CharField(max_length=140)
    slug = models.SlugField(default=f"title-{uuid.uuid4()}".lower(), unique=True)
    description = models.TextField()
    created_at = models.DateField(default=datetime.now())
    updated_at = models.DateField(default=datetime.now())

    def str(self):
        return self.title

    def default_slug(self):
        return self.title.lower().replace(" ", "-")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.default_slug()
        super().save(*args, **kwargs)


class Category(models.Model):
    category_id = models.UUIDField(
        unique=True,
        default=uuid.uuid4(),
        primary_key=True,
        editable=False,
        auto_created=True,
    )
    blogs = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category_title = models.CharField(max_length=55)
    created_at = models.DateField(default=datetime.now())
    updated_at = models.DateField(default=datetime.now())

    def str(self):
        return self.category_title


class Comment(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    posted_at = models.DateField(default=datetime.now())

    def str(self):
        return self.comment
