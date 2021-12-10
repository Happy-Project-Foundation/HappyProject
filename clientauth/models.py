from django.db import models
from django.contrib.auth.models import User

class Student(User):
    motto = models.CharField(verbose_name="Motto of a student", max_length=200)

    # TODO: add user preference
    
    is_staff = False
    is_active = True
    
    def __str__(self):
        return self.username
    
class Teacher(User):
    is_staff = True

    def __str__(self):
        return self.username
