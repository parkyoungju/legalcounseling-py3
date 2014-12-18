from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)