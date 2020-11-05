from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=14)
    summary = models.TextField(max_length=2000)
    degree  = models.CharField(max_length=80)
    school  = models.CharField(max_length=80)
    university = models.CharField(max_length=80, blank=True)
    previous_work = models.TextField(max_length=2000)
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.name



