from django.db import models
from authentication.models import User

#tu peut la modifier selon ton besoin ta logique de gestion de sang
class Blood(models.Model):
    blood_type_choices = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    
    blood_type = models.CharField(max_length=3, choices=blood_type_choices)
    quantity_ml = models.PositiveIntegerField()
    hospital = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'hospital'})
    date_donation = models.DateField()
    donor_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.blood_type} - {self.quantity_ml}ml - {self.date_donation} - Donor: {self.donor_name}"

# tt peut partager alert 
class Alert(models.Model):

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    besoin = models.TextField()
    age = models.PositiveIntegerField()
    GRAVITY_CHOICES = [
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('Severe', 'Severe'),
    ]
    gravite = models.CharField(max_length=10, choices=GRAVITY_CHOICES)
    tel_contact = models.CharField(max_length=20)
    ville = models.CharField(max_length=100)
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    type_sang = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Alerte - {self.nom} {self.prenom} - {self.type_sang}"