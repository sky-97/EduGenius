# assessments/models.py
from django.db import models
from django.utils import timezone

class Assessment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Set default value

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=255)
    assessment = models.ForeignKey(Assessment, related_name='questions', on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return self.text