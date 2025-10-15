# 📊 Dashboard de Suivi de Projets Techniques

Application web interactive pour le suivi et la visualisation de projets techniques multi-sites.

## 🎯 Objectif

Ce projet démontre la capacité à créer des outils de pilotage pour la gestion de projets techniques, similaires aux besoins de déploiement dans le secteur IT.

## ✨ Fonctionnalités

- **KPIs en temps réel** : Nombre de projets, taux de complétion, projets en retard, avancement moyen, satisfaction client
- **Visualisations interactives** :
  - Répartition par phase et par pays
  - Timeline des projets
  - Avancement détaillé par projet
  - Analyse de charge par responsable
- **Filtres dynamiques** : Par pays, phase, responsable et statut
- **Export de données** : Téléchargement CSV des données filtrées
- **Interface responsive** : Adaptation mobile et desktop

## 🛠️ Technologies Utilisées

- **Python 3.9+**
- **Streamlit** : Framework web pour data apps
- **Pandas** : Manipulation et analyse de données
- **Plotly** : Visualisations interactives
- **Openpyxl** : Lecture de fichiers Excel

## 📦 Installation

### Prérequis
- Python 3.9 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes

1. **Cloner le repository**
```bash
git clone https://github.com/thaise-steffani/project-dashboard.git
cd project-dashboard
```

2. **Créer un environnement virtuel (recommandé)**
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Préparer les données**
- Placez votre fichier `projets.xlsx` dans le dossier `data/`
- Ou utilisez le fichier d'exemple fourni

## 🚀 Utilisation

### Lancement local

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

### Utilisation de l'interface

1. **Filtres** : Utilisez la barre latérale pour filtrer les projets
2. **KPIs** : Consultez les indicateurs clés en haut de page
3. **Graphiques** : Interagissez avec les visualisations (zoom, hover, etc.)
4. **Tableau** : Triez et consultez les détails des projets
5. **Export** : Téléchargez les données filtrées en CSV

## 📊 Structure des Données

Le fichier Excel doit contenir les colonnes suivantes :

| Colonne | Type | Description |
|---------|------|-------------|
| Project_ID | Texte | Identifiant unique du projet |
| Client | Texte | Nom du client ou établissement |
| Pays | Texte | Pays du projet |
| Phase | Texte | Phase actuelle (Lancement, Installation, Formation, Clôture) |
| Responsable | Texte | Chef de projet assigné |
| Date_debut | Date | Date de début du projet |
| Date_fin | Date | Date de fin prévue |
| Status | Texte | Statut (En cours, Terminé, En retard) |
| Avancement | Nombre | Pourcentage d'avancement (0-100) |
| Satisfaction | Nombre | Score de satisfaction client (1-5) |

## 📁 Structure du Projet

```
project-dashboard/
│
├── data/
│   └── projets.xlsx          # Données des projets
│
├── app.py                     # Application principale
├── requirements.txt           # Dépendances Python
├── README.md                  # Documentation
└── .gitignore                # Fichiers ignorés par Git
```

## 🌐 Déploiement

### Streamlit Cloud (Gratuit)

1. Push votre code sur GitHub
2. Créez un compte sur [Streamlit Cloud](https://streamlit.io/cloud)
3. Connectez votre repository GitHub
4. Déployez en un clic
5. Obtenez votre URL publique

### Autres options
- **Heroku** : Pour un déploiement plus personnalisé
- **AWS/Azure/GCP** : Pour une infrastructure cloud complète

## 📈 Évolutions Futures

- [ ] Authentification utilisateur
- [ ] Base de données (PostgreSQL/MongoDB)
- [ ] API REST pour intégration
- [ ] Notifications automatiques (retards, jalons)
- [ ] Prédictions ML (risques de retard)
- [ ] Export PDF des rapports
- [ ] Mode dark/light

## Auteur

**Votre Nom**
- Portfolio : [votre-portfolio.com]
- LinkedIn : [linkedin.com/in/thaise-steffani]
- GitHub : [github.com/votre-thaise-steffani]

## Licence

Ce projet est un projet personnel à des fins de portfolio.


---

**Note** : Ce projet utilise des données fictives à des fins de démonstration. Aucune donnée réelle ou sensible n'est incluse.