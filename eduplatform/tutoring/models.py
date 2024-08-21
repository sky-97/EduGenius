from django.db import models

class TutoringSession(models.Model):
    subject = models.CharField(max_length=255)
    tutor = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    student = models.ForeignKey('users.CustomUser', related_name='students', on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject} - {self.tutor} with {self.student}'
