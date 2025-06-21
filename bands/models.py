from django.db import models
from django.utils import timezone

class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    booking_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    available_for_booking = models.BooleanField(default=True)
    image = models.ImageField(upload_to='band_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Concert(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    bands = models.ManyToManyField(Band)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.date})"
