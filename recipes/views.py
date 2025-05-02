# recipes/views.py
from recipes.models import Recette
from django.contrib import messages
from .forms import RecetteForm # Importer le ModelForm
from django.urls import reverse_lazy # Utilisé pour les redirections après succès



from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# READ - Liste des recettes
class RecetteListView(ListView):
    model = Recette # Le modèle à lister
    template_name = 'recipes/recette_list.html' # Le template à utiliser
    context_object_name = 'recettes' # Le nom de la variable dans le template (par défaut c'est object_list)

# READ - Détail d'une recette
class RecetteDetailView(DetailView):
    model = Recette
    template_name = 'recipes/recette_detail.html'
    # Par défaut, le nom de la variable dans le template est 'object' ou 'recette' (nom du modèle en minuscule)

# CREATE - Créer une nouvelle recette
class RecetteCreateView(CreateView):
    model = Recette
    form_class = RecetteForm
    template_name = 'recipes/recette_form.html'
    success_url = reverse_lazy('recette_list')
    
    def form_valid(self, form):
        # Cette méthode est appelée lorsque le formulaire est valide
        # Vous pouvez ajouter ici une logique supplémentaire avant l'enregistrement
        response = super().form_valid(form)
        
        # Exemple: Ajouter un message de succès
        messages.success(self.request, 'Recette créée avec succès!')
        
        return response
    
    def form_invalid(self, form):
        # Cette méthode est appelée lorsque le formulaire est invalide
        # Vous pouvez ajouter ici une logique supplémentaire
        messages.error(self.request, 'Veuillez corriger les erreurs ci-dessous.')
        return super().form_invalid(form)

# UPDATE - Modifier une recette existante
class RecetteUpdateView(UpdateView):
    model = Recette
    form_class = RecetteForm # Utilise le même ModelForm que pour la création
    template_name = 'recipes/recette_form.html' # Utilise le même template de formulaire
    # URL vers laquelle rediriger après avoir modifié la recette avec succès
    # Peut rediriger vers la page de détail de la recette modifiée ou la liste
    # success_url = reverse_lazy('recette_detail', pk=self.object.pk) # Example de redirection vers le détail (nécessite override get_success_url)
    success_url = reverse_lazy('recette_list') # Pour l'exemple, redirigeons vers la liste

    # Si vous voulez rediriger vers la page de détail de la recette modifiée:
    # def get_success_url(self):
    #    return reverse_lazy('recette_detail', kwargs={'pk': self.object.pk})


# DELETE - Supprimer une recette
class RecetteDeleteView(DeleteView):
    model = Recette
    template_name = 'recipes/recette_confirm_delete.html' # Template pour la page de confirmation
    # URL vers laquelle rediriger après avoir supprimé la recette avec succès
    success_url = reverse_lazy('recette_list') # Redirige vers la liste des recettes après suppression