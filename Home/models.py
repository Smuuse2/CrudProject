from django.db import models

class Student(models.Model):
    sid = models.CharField(max_length=300)
    sname = models.CharField(max_length=300)
    scontact = models.CharField(max_length=300)

    def __str__(self):
        return self.sname

# Create your models here.
