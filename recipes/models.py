from django.db import models

# Create your models here.

class Recette(models.Model):
    nom = models.CharField(max_length=200)
    description_courte = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    cout_estime = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='recettes/', blank=True, null=True)

    def __str__(self):
        return self.nom