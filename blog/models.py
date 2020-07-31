# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200)
    # text = models.TextField()
    text = RichTextField(blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='posts_images', null=True, blank=True)

    def __str__(self):
        return self.title
