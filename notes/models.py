from django.db import models
from django.conf import settings


class Note(models.Model):
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255, default='None')
    fragment = models.TextField(max_length=255, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # change modified to update on change (see docs!)
    modified = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
