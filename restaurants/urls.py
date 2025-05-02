from django.urls import path
from . import views

urlpatterns = [
    # path('', views.liste_restaurants, name='liste_restaurants'), # Si vous voulez une liste indépendante
    # path('<int:pk>/', views.detail_restaurant, name='detail_restaurant'), # ex: /restaurants/1/
    # Pour ce projet, vous n'avez peut-être pas besoin de vues/templates de détail restaurant séparés tout de suite.
    # La liste dans resultats.html pourrait suffire.
]