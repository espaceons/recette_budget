from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('resultats/', views.resultats, name='resultats'),
]