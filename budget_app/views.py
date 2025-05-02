# budget_app/views.py
from django.shortcuts import render, redirect
from .forms import BudgetForm
# Importe les modèles des autres applications
from recipes.models import Recette
from restaurants.models import Restaurant


def about (request):
    return render(request,'budget_app/about.html')

def contact (request):
    return render(request,'budget_app/contact.html')

def privacy (request):
    return render(request,'budget_app/privacy.html')

def accueil(request):
    # Logique du formulaire et de la redirection avec session (comme vue unique précédente)
    # ... (voir exemple précédent)
     if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            montant = form.cleaned_data['montant']
            choix = form.cleaned_data['choix']
            request.session['montant'] = str(montant)
            request.session['choix'] = choix
            return redirect('resultats')
     else:
        form = BudgetForm()
        if 'montant' in request.session: del request.session['montant']
        if 'choix' in request.session: del request.session['choix']

     return render(request, 'budget_app/accueil.html', {'form': form})


def resultats(request):
    montant = request.session.get('montant')
    choix = request.session.get('choix')

    if montant is None or choix is None:
        return redirect('accueil')

    try:
        montant = float(montant)
    except ValueError:
        return redirect('accueil')

    recettes = []
    restaurants = []
    message = ""

    if choix == 'recette':
        # Utilise le modèle Recette de l'application recipes
        recettes = Recette.objects.filter(cout_estime__lte=montant).order_by('cout_estime')
        if not recettes:
            message = "Aucune recette trouvée pour ce budget."

    elif choix == 'restaurant':
        # Utilise le modèle Restaurant de l'application restaurants
        if montant < 10: gamme_visee = '$'
        elif 10 <= montant < 30: gamme_visee = '$$'
        else: gamme_visee = '$$$'

        gammes_abordables = []
        if gamme_visee == '$$$': gammes_abordables.extend(['$', '$$', '$$$'])
        elif gamme_visee == '$$': gammes_abordables.extend(['$', '$$'])
        else: gammes_abordables.append('$')

        # Utilise le modèle Restaurant de l'application restaurants
        restaurants = Restaurant.objects.filter(gamme_prix__in=gammes_abordables)

        if not restaurants:
             message = "Aucun restaurant trouvé pour ce budget dans les gammes de prix correspondantes."

    if 'montant' in request.session: del request.session['montant']
    if 'choix' in request.session: del request.session['choix']

    context = {
        'montant': montant,
        'choix': choix,
        'recettes': recettes,
        'restaurants': restaurants,
        'message': message,
    }

    return render(request, 'budget_app/resultats.html', context)

# Pas de vue detail_recette ou detail_restaurant ici, elles sont dans leurs apps respectives