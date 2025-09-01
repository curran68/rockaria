from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as needed, e.g.:
    # event_date = models.DateTimeField()
    # price = models.DecimalField(max_digits=8, decimal_places=2)
    # description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.ticket.name} ({self.purchase_date})"
