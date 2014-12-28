from django.db import models


class Essay(models.Model):
    title = models.CharField(max_length=255, default='', blank=False)
    content = models.CharField(max_length=255, default='', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
