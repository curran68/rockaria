from django.db import models
from django.utils import timezone

class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Concert(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    bands = models.ManyToManyField(Band)
    created_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.date})"
