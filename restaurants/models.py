from django.db import models

from django.db import models

class Restaurant(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    gamme_prix_choix = [
        ('SIM', 'Économique'),
        ('MOY', 'Modéré'),
        ('LUX', 'Cher'),
    ]
    gamme_prix = models.CharField(max_length=5, choices=gamme_prix_choix, default='$')
    type_cuisine = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom