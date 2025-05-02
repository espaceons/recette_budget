# budget_app/forms.py
from django import forms

CHOIX_OPTIONS = [
    ('recette', 'Préparer un repas'),
    ('restaurant', 'Aller au restaurant'),
]

class BudgetForm(forms.Form):
    # Champ pour le montant d'argent
    montant = forms.DecimalField(
        label="Votre budget",         # Libellé affiché à l'utilisateur
        max_digits=6,                 # Nombre total de chiffres (avant et après la virgule)
        decimal_places=2,             # Nombre de chiffres après la virgule
        min_value=0.01,               # La valeur doit être supérieure à 0
        # Widget HTML pour améliorer l'interface
        widget=forms.NumberInput(attrs={'placeholder': 'Ex: 15.50', 'step': '0.01'})
    )

    # Champ pour le choix (recette ou restaurant)
    choix = forms.ChoiceField(
        label="Que voulez-vous faire ?",
        choices=CHOIX_OPTIONS,        # Options possibles basées sur la liste définie plus haut
        widget=forms.RadioSelect      # Afficher les options sous forme de boutons radio
    )