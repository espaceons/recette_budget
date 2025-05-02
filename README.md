
![Capture d’écran 2025-05-02 121319](https://github.com/user-attachments/assets/d303b88a-c6af-4c1e-af1f-cdb5a9ef0b80)




L'application web a pour but d'aider les utilisateurs à optimiser leur budget alimentaire. En entrant un montant d’argent, l’utilisateur peut :

Cuisiner un repas adapté à son budget grâce à des recettes détaillées.

Trouver un restaurant proche qui propose des plats correspondant à ce montant.

 Fonctionnalités principales
💰 Saisie du budget (par exemple : "J’ai 15 dinars").

🥘 Suggestions de recettes en fonction du montant :

Liste d'ingrédients

Coût estimé

Instructions de préparation

📍 Suggestions de restaurants à proximité :

Utilisation de la géolocalisation

Affichage des restaurants avec prix moyen

🔍 Filtrage intelligent : recettes végétariennes, rapides, familiales, etc.

🔐 Authentification utilisateur (optionnelle) pour sauvegarder ses préférences.


Technologies utilisées
Back-end : Django (Python)

Front-end : HTML, Bootstrap, JavaScript

Base de données : SQLite (développement) / PostgreSQL (production)

Géolocalisation : API HTML5 ou Google Places (optionnel)

Design responsive : compatible mobile et desktop




Organisation du projet Django
recettes : gestion des recettes et ingrédients

restaurants : gestion des lieux et suggestions

utilisateurs : gestion de comptes et préférences (optionnel)

core : pages d’accueil, gestion du budget, logique centrale



Exemple d’utilisation
L'utilisateur arrive sur la page d’accueil.

Il entre un montant : "J’ai 10 dinars"

Il choisit entre :

Cuisiner : la plateforme lui propose 3 recettes avec instructions.

Sortir : l'application lui montre les restaurants proches où il peut manger pour ce prix.
