from django.db import models
from authentication.models import User
from associations.models import Event

class RendezVous(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    citizen = models.ForeignKey(User, on_delete=models.CASCADE)
    heure_rdv = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.event} - {self.citizen} - {self.heure_rdv}"



class Notification(models.Model):
    TYPE_CHOICES = [
        ('Reminder', 'Reminder'),
        ('Information', 'Information'),
    ]

    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.event} - {self.recipient}"