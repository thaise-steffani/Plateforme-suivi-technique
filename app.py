import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(
    page_title="Dashboard Suivi Projets",
    page_icon="📊",
    layout="wide"
)

# Titre principal
st.title("📊 Dashboard de Suivi de Projets Techniques")
st.markdown("---")

# Fonction pour charger les données
@st.cache_data
def load_data():
    """Charge et prépare les données depuis Excel"""
    try:
        df = pd.read_excel('data/projets.xlsx')
        
        # Conversion des dates
        df['Date_debut'] = pd.to_datetime(df['Date_debut'])
        df['Date_fin'] = pd.to_datetime(df['Date_fin'])
        
        # Calcul des jours restants
        today = datetime.now()
        df['Jours_restants'] = (df['Date_fin'] - today).dt.days
        
        # Détection des retards
        df['En_retard'] = (df['Jours_restants'] < 0) & (df['Status'] == 'En cours')
        
        return df
    except FileNotFoundError:
        st.error("❌ Fichier 'data/projets.xlsx' non trouvé. Veuillez vérifier le chemin.")
        st.stop()

# Chargement des données
df = load_data()

# Sidebar - Filtres
st.sidebar.header("🔍 Filtres")

# Filtre par pays
pays_options = ['Tous'] + sorted(df['Pays'].unique().tolist())
pays_selectionne = st.sidebar.selectbox("Pays", pays_options)

# Filtre par phase
phase_options = ['Tous'] + sorted(df['Phase'].unique().tolist())
phase_selectionnee = st.sidebar.selectbox("Phase", phase_options)

# Filtre par responsable
responsable_options = ['Tous'] + sorted(df['Responsable'].unique().tolist())
responsable_selectionne = st.sidebar.selectbox("Responsable", responsable_options)

# Filtre par status
status_options = ['Tous'] + sorted(df['Status'].unique().tolist())
status_selectionne = st.sidebar.selectbox("Status", status_options)

# Application des filtres
df_filtre = df.copy()

if pays_selectionne != 'Tous':
    df_filtre = df_filtre[df_filtre['Pays'] == pays_selectionne]

if phase_selectionnee != 'Tous':
    df_filtre = df_filtre[df_filtre['Phase'] == phase_selectionnee]

if responsable_selectionne != 'Tous':
    df_filtre = df_filtre[df_filtre['Responsable'] == responsable_selectionne]

if status_selectionne != 'Tous':
    df_filtre = df_filtre[df_filtre['Status'] == status_selectionne]

# KPIs en haut de page
st.subheader("📈 Indicateurs Clés")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Projets", len(df_filtre))

with col2:
    projets_termines = len(df_filtre[df_filtre['Status'] == 'Terminé'])
    taux_completion = (projets_termines / len(df_filtre) * 100) if len(df_filtre) > 0 else 0
    st.metric("Taux Complétion", f"{taux_completion:.1f}%")

with col3:
    projets_retard = df_filtre['En_retard'].sum()
    st.metric("Projets en Retard", projets_retard, delta=None, delta_color="inverse")

with col4:
    avancement_moyen = df_filtre['Avancement'].mean()
    st.metric("Avancement Moyen", f"{avancement_moyen:.1f}%")

with col5:
    satisfaction_moyenne = df_filtre['Satisfaction'].mean()
    st.metric("Satisfaction", f"{satisfaction_moyenne:.1f}/5", delta=None)

st.markdown("---")

# Section des graphiques
col_gauche, col_droite = st.columns(2)

# Graphique 1: Projets par phase
with col_gauche:
    st.subheader("📊 Répartition par Phase")
    phase_counts = df_filtre['Phase'].value_counts().reset_index()
    phase_counts.columns = ['Phase', 'Nombre']
    
    fig_phase = px.bar(
        phase_counts,
        x='Phase',
        y='Nombre',
        color='Phase',
        text='Nombre',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_phase.update_traces(textposition='outside')
    fig_phase.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig_phase, use_container_width=True)

# Graphique 2: Projets par pays
with col_droite:
    st.subheader("🌍 Répartition Géographique")
    pays_counts = df_filtre['Pays'].value_counts().reset_index()
    pays_counts.columns = ['Pays', 'Nombre']
    
    fig_pays = px.pie(
        pays_counts,
        values='Nombre',
        names='Pays',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_pays.update_layout(height=400)
    st.plotly_chart(fig_pays, use_container_width=True)

# Graphique 3: Avancement par projet
st.subheader("📈 Avancement des Projets")
fig_avancement = px.bar(
    df_filtre.sort_values('Avancement', ascending=True),
    x='Avancement',
    y='Project_ID',
    orientation='h',
    color='Status',
    text='Avancement',
    color_discrete_map={
        'En cours': '#FFA500',
        'Terminé': '#4CAF50',
        'En retard': '#F44336'
    }
)
fig_avancement.update_traces(texttemplate='%{text}%', textposition='outside')
fig_avancement.update_layout(height=400, showlegend=True)
st.plotly_chart(fig_avancement, use_container_width=True)

# Timeline des projets
st.subheader("📅 Timeline des Projets")
fig_timeline = px.timeline(
    df_filtre,
    x_start='Date_debut',
    x_end='Date_fin',
    y='Project_ID',
    color='Phase',
    hover_data=['Client', 'Responsable', 'Avancement']
)
fig_timeline.update_layout(height=400)
st.plotly_chart(fig_timeline, use_container_width=True)

# Analyse par responsable
st.subheader("👥 Charge de Travail par Responsable")
col_resp1, col_resp2 = st.columns(2)

with col_resp1:
    responsable_counts = df_filtre['Responsable'].value_counts().reset_index()
    responsable_counts.columns = ['Responsable', 'Nombre_Projets']
    
    fig_resp = px.bar(
        responsable_counts,
        x='Responsable',
        y='Nombre_Projets',
        text='Nombre_Projets',
        color='Nombre_Projets',
        color_continuous_scale='Blues'
    )
    fig_resp.update_traces(textposition='outside')
    fig_resp.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig_resp, use_container_width=True)

with col_resp2:
    satisfaction_resp = df_filtre.groupby('Responsable')['Satisfaction'].mean().reset_index()
    satisfaction_resp.columns = ['Responsable', 'Satisfaction_Moyenne']
    
    fig_sat_resp = px.bar(
        satisfaction_resp,
        x='Responsable',
        y='Satisfaction_Moyenne',
        text='Satisfaction_Moyenne',
        color='Satisfaction_Moyenne',
        color_continuous_scale='RdYlGn',
        range_color=[1, 5]
    )
    fig_sat_resp.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig_sat_resp.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig_sat_resp, use_container_width=True)

# Tableau détaillé
st.markdown("---")
st.subheader("📋 Détails des Projets")

# Préparation du tableau
df_display = df_filtre[[
    'Project_ID', 'Client', 'Pays', 'Phase', 'Responsable',
    'Date_debut', 'Date_fin', 'Status', 'Avancement', 'Satisfaction'
]].copy()

# Formatage des dates
df_display['Date_debut'] = df_display['Date_debut'].dt.strftime('%d/%m/%Y')
df_display['Date_fin'] = df_display['Date_fin'].dt.strftime('%d/%m/%Y')

# Affichage avec possibilité de tri
st.dataframe(
    df_display,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Avancement": st.column_config.ProgressColumn(
            "Avancement",
            format="%d%%",
            min_value=0,
            max_value=100,
        ),
        "Satisfaction": st.column_config.NumberColumn(
            "Satisfaction",
            format="⭐ %.1f",
            min_value=1,
            max_value=5,
        )
    }
)

# Export des données
st.markdown("---")
st.subheader("💾 Export des Données")

# Bouton d'export CSV
csv = df_filtre.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Télécharger les données filtrées (CSV)",
    data=csv,
    file_name=f'projets_export_{datetime.now().strftime("%Y%m%d")}.csv',
    mime='text/csv',
)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <p>Dashboard de Suivi de Projets Techniques | Développé avec Streamlit & Python</p>
        <p>Projet Portfolio 2025</p>
    </div>
    """,
    unsafe_allow_html=True
)
