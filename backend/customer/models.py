from django.db import models

class Customer(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=[('Actif', 'Actif'), ('Inactif', 'Inactif')])

    def __str__(self):
        return self.nom
