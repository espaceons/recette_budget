# recipes/urls.py
from django.urls import path
from . import views # Importer vos vues (qui seront les CBVs)

urlpatterns = [
    # READ (Liste) : Affiche toutes les recettes
    path('', views.RecetteListView.as_view(), name='recette_list'),

    # CREATE : Affiche un formulaire pour créer une nouvelle recette
    path('ajouter/', views.RecetteCreateView.as_view(), name='recette_create'),

    # READ (Détail) : Affiche une recette spécifique (utilise la clé primaire pk)
    # Le chemin doit être APRÈS 'ajouter/' sinon 'ajouter' serait interprété comme un pk
    path('<int:pk>/', views.RecetteDetailView.as_view(), name='recette_detail'),

    # UPDATE : Affiche un formulaire pour modifier une recette existante
    path('<int:pk>/modifier/', views.RecetteUpdateView.as_view(), name='recette_update'),

    # DELETE : Affiche une page de confirmation pour supprimer une recette
    path('<int:pk>/supprimer/', views.RecetteDeleteView.as_view(), name='recette_delete'),
]