# recipes/forms.py
from django import forms
from recipes.models import Recette

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        # Liste des champs du modèle que vous voulez inclure dans le formulaire
        # __all__ inclut tous les champs du modèle
        # Ou liste spécifique : fields = ['nom', 'description_courte', 'ingredients', 'instructions', 'cout_estime', 'image']
        fields = '__all__'
        # Optionnel: vous pouvez ajouter des widgets pour personnaliser l'apparence des champs HTML
        widgets = {
             'ingredients': forms.Textarea(attrs={'rows': 4}),
             'instructions': forms.Textarea(attrs={'rows': 6}),
             'cout_estime': forms.NumberInput(attrs={'step': '0.01'}),
         }
        
        
    def clean(self):
        cleaned_data = super().clean()
        # Ajoutez ici des validations personnalisées si nécessaire
        return cleaned_data