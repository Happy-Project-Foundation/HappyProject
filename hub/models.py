import uuid

from django.db import models

from watchdog.models import HappyPerson


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
    subject = models.CharField(verbose_name="Subject", max_length=20, choices=_subjects, blank=False,
                               default=_subjects[0][1])
    type = models.CharField(verbose_name="Type", max_length=45, choices=_types, blank=False, default=_types[0][1])

    def __str__(self) -> str:
        return self.title


class Student(models.Model):
    student = models.OneToOneField(HappyPerson, on_delete=models.CASCADE)
    subjects = models.TextField(verbose_name="Subjects a student follows")
    resources = models.TextField(verbose_name="Resources a student needs")
    school = models.CharField(verbose_name="School student belongs to", max_length=100,
                              default="St. Patrick's College, Jaffna")
    country = models.CharField(verbose_name="Country student belongs to", max_length=100, default="Sri Lanka")
    motto = models.CharField(verbose_name="A self assigned motto", max_length=255,
                             default="We work in dark to save the light")
    language = models.CharField(verbose_name="Language student preferes", max_length=5, default="en_US")
    age = models.IntegerField(verbose_name="Age of the student", default=18)

    def __str__(self):
        return self.student.email