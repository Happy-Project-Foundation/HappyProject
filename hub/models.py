import uuid

from django.db import models


class Resource(models.Model):

    _types = [
        ("Department(Sri Lanka) of Examinations Paper", "Department(Sri Lanka) of Examinations Paper"),
        ("Pilot Papers", "Pilot Papers"),
        ("Happy Community Issues", "Happy Community Issues"),
        ("Tutorials", "Tutorials"),
        ("Others", "Others"),
    ]

    _subjects = [
        ("ICT", "ICT"),
        ("Pure Mathematics", "Pure Mathematics"),
        ("Applied Mathematics", "Applied Mathematics"),
        ("Physics", "Physics"),
        ("General English", "General English"),
        ("IQ", "IQ"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    title = models.CharField(verbose_name="Title", max_length=15, blank=False, default="A title")
    desc = models.CharField(verbose_name="Description", max_length=50, blank=False, default="A description")
    link = models.URLField(verbose_name="URL", max_length=300, blank=False,
                           null=False, default="https://github.com/BirnadinErick/HappyProject")
    subject = models.CharField(verbose_name="Subject", max_length=20, choices=_subjects, blank=False, default=_subjects[0][1])
    type = models.CharField(verbose_name="Type", max_length=45, choices=_types, blank=False, default=_types[0][1])

    def __str__(self) -> str:
        return f"{self.title}"
