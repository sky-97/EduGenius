# tutoring/models.py
from django.db import models

class TutoringSession(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
