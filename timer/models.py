import uuid

from django.db import models
from django.utils import timezone
from django.conf import settings


class Puzzle(models.Model):
    name = models.TextField(unique=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Solve(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    centiseconds = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    comments = models.TextField(null=True)
    puzzle = models.ForeignKey(
        Puzzle,
        on_delete=models.CASCADE,
        null=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.centiseconds/100) + ' seconds on ' + str(self.date)
