from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    response_email = models.EmailField()
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text[:60]
