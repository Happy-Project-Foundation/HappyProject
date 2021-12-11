import uuid

from django.db import models
from django.db.models.fields import TextField


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name="Title", max_length=150, default="Happy Blog", blank=False)
    content = models.TextField(verbose_name="Content:", max_length=500, blank=False, default="Happy Content")
    summary = models.TextField(verbose_name="Summary", max_length=300,
    blank=True)

    def __str__(self):
        return self.title
    
