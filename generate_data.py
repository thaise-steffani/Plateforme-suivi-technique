"""
Script pour générer le fichier Excel de données d'exemple
Exécutez ce script une seule fois pour créer projets.xlsx
"""

import pandas as pd
from datetime import datetime, timedelta
import random
import os

# Configuration
random.seed(42)  # Pour reproductibilité

# Créer le dossier data s'il n'existe pas
if not os.path.exists('data'):
    os.makedirs('data')
    print("✅ Dossier 'data/' créé")

# Données de base
clients = [
    'Hôpital Saint', 'Clinique', 'CHU', 'Polyclinique',
    'Hospital General', 'Hospital', 'Klinikum', 'CHU M',
    'Clinic', 'General', 'Clinique Q', 'Hôpital P',
    'Hospital B', 'University Hospital', 'Clinique', 'CHU L',
    'Medical Center', 'Hospital D', 'CHU N', 'Hospital C'
]

pays = [
    'France', 'France', 'France', 'France', 'Espagne', 'UK', 'Allemagne', 'France',
    'USA', 'Canada', 'Suisse', 'France', 'Espagne', 'USA', 'Belgique', 'France',
    'Australie', 'UAE', 'France', 'USA'
]

phases = [
    'Installation', 'Formation', 'Lancement', 'Clôture', 'Installation', 
    'Formation', 'Lancement', 'Installation', 'Clôture', 'Installation',
    'Formation', 'Lancement', 'Installation', 'Clôture', 'Formation',
    'Lancement', 'Installation', 'Formation', 'Clôture', 'Installation'
]

responsables = [
    'Sophie', 'Jean ', 'Marie ', 'Sophie ', 'Pierre ',
    'Jean ', 'Marie ', 'Sophie ', 'Pierre ', 'Jean ',
    'Marie ', 'Sophie ', 'Pierre ', 'Jean ', 'Marie ',
    'Sophie ', 'Pierre ', 'Jean ', 'Marie ', 'Sophie '
]

# Génération des données
data = []
base_date = datetime.now()

for i in range(20):
    # Génération des dates
    jours_debut = random.randint(-60, 30)
    date_debut = base_date + timedelta(days=jours_debut)
    
    duree = random.randint(30, 120)
    date_fin = date_debut + timedelta(days=duree)
    
    # Attribution du status et avancement selon la phase
    phase = phases[i]
    
    if phase == 'Clôture':
        status = 'Terminé'
        avancement = 100
        satisfaction = round(random.uniform(4.0, 5.0), 1)
    elif phase == 'Lancement':
        status = 'En cours'
        avancement = random.randint(15, 35)
        satisfaction = round(random.uniform(3.5, 4.5), 1)
    elif phase == 'Installation':
        status = 'En cours'
        avancement = random.randint(40, 70)
        satisfaction = round(random.uniform(3.8, 4.8), 1)
    else:  # Formation
        status = 'En cours'
        avancement = random.randint(75, 95)
        satisfaction = round(random.uniform(4.0, 4.8), 1)
    
    # Ajout du projet
    data.append({
        'Project_ID': f'P{str(i + 1).zfill(3)}',
        'Client': clients[i],
        'Pays': pays[i],
        'Phase': phase,
        'Responsable': responsables[i],
        'Date_debut': date_debut,
        'Date_fin': date_fin,
        'Status': status,
        'Avancement': avancement,
        'Satisfaction': satisfaction
    })

# Création du DataFrame
df = pd.DataFrame(data)

# Affichage d'un aperçu
print("\n📊 Aperçu des données générées:")
print("="*80)
print(df.head(10).to_string(index=False))
print("="*80)
print(f"\n📈 Statistiques:")
print(f"   • Total projets: {len(df)}")
print(f"   • En cours: {len(df[df['Status'] == 'En cours'])}")
print(f"   • Terminés: {len(df[df['Status'] == 'Terminé'])}")
print(f"   • Avancement moyen: {df['Avancement'].mean():.1f}%")
print(f"   • Satisfaction moyenne: {df['Satisfaction'].mean():.2f}/5")
print(f"   • Pays représentés: {df['Pays'].nunique()}")

# Sauvegarde en Excel
output_file = 'data/projets.xlsx'
df.to_excel(output_file, index=False, sheet_name='Projets')

print(f"\n✅ Fichier '{output_file}' créé avec succès!")
print(f"📁 Emplacement: {os.path.abspath(output_file)}")
print("\n🚀 Vous pouvez maintenant lancer l'application avec: streamlit run app.py")
