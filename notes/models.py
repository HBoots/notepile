from django.db import models
from django.conf import settings
from django.urls import reverse
import uuid


class Note(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True,
                          default=uuid.uuid4, editable=False, verbose_name='ID')
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255, default='Other')
    fragment = models.TextField(max_length=255, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail', args=[str(self.id)])


class File(models.Model):
    file = models.FileField(upload_to='json_files/')
