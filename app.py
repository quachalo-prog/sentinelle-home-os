import streamlit as st
import pandas as pd
import time
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Sentinelle Home OS",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Gestion du thème (Clair / Sombre) via la session Streamlit
if 'theme' not in st.session_state:
    st.session_state.theme = 'sombre'

# Fonction pour changer de thème
def toggle_theme():
    st.session_state.theme = 'clair' if st.session_state.theme == 'sombre' else 'sombre'

# Application des styles CSS dynamiques selon le thème choisi
if st.session_state.theme == 'clair':
    # --- THÈME PURETÉ MODERNE (CLAIR) ---
    st.markdown("""
    <style>
        .main { background-color: #f8f9fa; }
        .stApp { background-color: #f8f9fa; color: #0f172a; }
        h1, h2, h3 { color: #0f172a; font-family: 'Helvetica Neue', Arial, sans-serif; }
        .card {
            background-color: white;
            padding: 18px;
            border-radius: 12px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02), 0 1px 2px rgba(0,0,0,0.05);
            margin-bottom: 15px;
            border-left: 5px solid #2563eb;
            color: #1e293b;
        }
        .card-critical { border-left-color: #ef4444; background-color: #fef2f2; }
        .card-warning { border-left-color: #f59e0b; background-color: #fffbeb; }
        .card-info { border-left-color: #2563eb; background-color: #eff6ff; }
        .card-success { border-left-color: #10b981; background-color: #ecfdf5; }
        .feed-time { font-size: 0.85em; color: #64748b; font-weight: bold; }
        .badge { padding: 3px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold; display: inline-block; }
        .badge-critical { background-color: #fee2e2; color: #991b1b; }
        .badge-warning { background-color: #fef3c7; color: #92400e; }
        .badge-info { background-color: #dbeafe; color: #1e40af; }
        .badge-success { background-color: #d1fae5; color: #065f46; }
    </style>
    """, unsafe_allow_html=True)
else:
    # --- THÈME SENTINELLE NOCTURNE (SOMBRE) ---
    st.markdown("""
    <style>
        .main { background-color: #0f172a; }
        .stApp { background-color: #0f172a; color: #f1f5f9; }
        h1, h2, h3 { color: #f8fafc; font-family: 'Helvetica Neue', Arial, sans-serif; }
        .card {
            background-color: #1e293b;
            padding: 18px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
            margin-bottom: 15px;
            border-left: 5px solid #3b82f6;
            color: #e2e8f0;
        }
        .card-critical { border-left-color: #ef4444; background-color: #2d1a1a; }
        .card-warning { border-left-color: #f59e0b; background-color: #2d241a; }
        .card-info { border-left-color: #3b82f6; background-color: #1a2333; }
        .card-success { border-left-color: #10b981; background-color: #1a2d24; }
        .feed-time { font-size: 0.85em; color: #94a3b8; font-weight: bold; }
        .badge { padding: 3px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold; display: inline-block; }
        .badge-critical { background-color: #7f1d1d; color: #fca5a5; }
        .badge-warning { background-color: #78350f; color: #fcd34d; }
        .badge-info { background-color: #1e3a8a; color: #93c5fd; }
        .badge-success { background-color: #064e3b; color: #6ee7b7; }
    </style>
    """, unsafe_allow_html=True)

# Barre latérale de navigation haut de gamme
st.sidebar.title("🛡️ Sentinelle Home OS")
st.sidebar.markdown("*Intelligence, Éthique & Haute Sécurité*")
st.sidebar.write("---")

# Simulation de l'accès Biométrique Rapide (Face ID / Empreinte)
if 'biometry_authenticated' not in st.session_state:
    st.session_state.biometry_authenticated = False

if not st.session_state.biometry_authenticated:
    st.sidebar.warning("🔒 Verrouillé par biométrie")
    if st.sidebar.button("👆 Utiliser Face ID / Empreinte"):
        st.session_state.biometry_authenticated = True
        st.sidebar.success("🔓 Authentification réussie")
        st.rerun()
    st.title("🛡️ Sentinelle Home OS — Accès Sécurisé")
    st.info("Veuillez utiliser le module d'authentification rapide sur la gauche pour déverrouiller l'application sur votre smartphone.")
    st.stop()

# Bouton de changement de style (Soleil / Lune) tout en haut de la barre latérale
theme_icon = "☀️ Mode Clair" if st.session_state.theme == 'sombre' else "🌙 Mode Sombre"
st.sidebar.button(theme_icon, on_click=toggle_theme)

menu = st.sidebar.radio(
    "Navigation",
    ["📊 Fil narratif", "🎥 Direct & Caméras", "⚙️ Alertes & Cascade", "🐾 Paramètres Animaux"]
)

st.sidebar.write("---")
st.sidebar.subheader("Santé du Système")
st.sidebar.success("● Moteur IA Local Actif")

# --- ÉCRAN 1 : FIL NARRATIF (FEED) ---
if menu == "📊 Fil narratif":
    st.title("📊 Fil Narratif de la Maison")
    st.markdown("Chronologie intelligente en langage naturel générée en temps réel par l'IA.")
    
    search_query = st.text_input("🔍 Recherche sémantique (ex: 'Léo', 'Chien', 'Coupure')", "")
    
    # Données enrichies intégrant l'horodatage précis à la seconde
    events = [
        {"time": "14:32:08", "type": "critical", "cat": "RÉSEAU", "text": "[CRITIQUE] Perte de connexion détectée sur la 'Caméra Cuisine'. Raison probable : Coupure d'alimentation ou débranchement physique.", "tag": "Alerte Système"},
        {"time": "12:15:34", "type": "warning", "cat": "ENFANTS", "text": "Léo s'est approché de la zone interdite 'Escalier'. Signal sonore local émis automatiquement. L'enfant a reculé.", "tag": "Danger Évité"},
        {"time": "11:40:12", "type": "info", "cat": "ANIMAUX", "text": "Résumé d'activité : Le chien a passé la matinée sur son panier du salon. Activité calme.", "tag": "Journal de bord"},
        {"time": "08:45:21", "type": "critical", "cat": "SÉNIORS", "text": "Alerte Chute annulée : Posture suspecte détectée dans le salon, mais l'utilisateur a répondu 'Tout va bien' lors de la levée de doute vocale.", "tag": "Urgence Évitée"}
    ]
    
    if search_query:
        events = [e for e in events if search_query.lower() in e['text'].lower() or search_query.lower() in e['cat'].lower()]
        
    for e in events:
        st.markdown(f"""
        <div class="card card-{e['type']}">
            <span class="feed-time">{e['time']}</span> | <span class="badge badge-{e['type']}">{e['cat']}</span> <span class="badge badge-info">{e['tag']}</span>
            <div style="margin-top:7px; font-weight:500;">{e['text']}</div>
        </div>
        """, unsafe_allow_html=True)

# --- ÉCRAN 2 : DIRECT & CAMÉRAS (CONNEXION SIMPLIFIÉE) ---
elif menu == "🎥 Direct & Caméras":
    st.title("🎥 Flux en Direct & Centralisation")
    st.markdown("Visualisez vos caméras en direct sans passer par les applications constructeurs.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Visualisation Multi-View")
        st.image("https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=800&q=80", 
                 caption="Flux Salon / Cuisine - Analyse en direct via IA Locale", use_container_width=True)
        
        st.markdown("💡 *Glissez virtuellement votre doigt sur l'image pour remonter le temps grâce à l'indexation sémantique.*")
        
    with col2:
        st.subheader("🔌 Connexion Express")
        st.write("Ajoutez n'ici n'importe quelle caméra Wi-Fi du marché.")
        
        if st.button("🔄 Scanner le réseau Wi-Fi de la maison"):
            with st.spinner("Recherche de flux RTSP / ONVIF disponibles..."):
                time.sleep(1.5)
                st.success("2 caméras trouvées automatiquement (Salon, Entrée) !")
                
        st.write("---")
        st.subheader("🛡️ Protection Éthique")
        ethique = st.checkbox("Activer le rendu Squelette 3D pour la chambre parentale (Respect strict de la vie privée)", value=True)
        if ethique:
            st.info("Mode Éthique : L'image vidéo brute est détruite localement, seul le squelette fil de fer est analysé.")

# --- ÉCRAN 3 : ALERTES & CASCADE ---
elif menu == "⚙️ Alertes & Cascade":
    st.title("⚙️ Sécurité Critique & Déconnexions")
    st.markdown("Configurez la réactivité de votre Sentinelle face aux dangers majeurs.")
    
    st.subheader("Alerte Enfant Maximale")
    st.write("Lorsqu'un enfant franchit une zone interdite (dessinée sur la caméra) :")
    st.success("✔️ Émission d'un son dissuasif immédiat sur la caméra locale.")
    st.success("✔️ Envoi d'une notification FLASH sur le smartphone (outrepasse le mode silencieux).")
    
    st.write("---")
    st.subheader("Surveillance Réseau (Anti-Sabotage)")
    st.write("Si une caméra est débranchée ou perd sa connexion internet :")
    st.checkbox("M'alerter immédiatement avec horodatage précis à la seconde", value=True, disabled=True)
    
    if st.button("🚨 Déclencher une simulation de panne réseau (Test)"):
        current_time = datetime.now().strftime("%H:%M:%S")
        st.error(f"🚨 ALERT SYSTÈME à {current_time} — Perte de signal immédiate sur 'Caméra Entrée'. Notification de secours transmise.")

# --- ÉCRAN 4 : PARAMÈTRES ANIMAUX ---
elif menu == "🐾 Paramètres Animaux":
    st.title("🐾 Intelligence Animale Paramétrable")
    st.markdown("Choisissez comment vous désirez suivre les comportements de vos animaux de compagnie.")
    
    mode_animal = st.radio(
        "Mode de notification pour vos animaux :",
        [
            "📱 Mode Live Tracker (Notifications instantanées en temps réel en cas de bêtise ou comportement suspect)",
            "📅 Mode Journal de Bord (Résumé global envoyé proprement chaque soir sous forme de rapport d'activité)"
        ]
    )
    
    st.write("---")
    st.subheader("Aperçu du Journal de Bord Animal (Exemple)")
    st.info("📝 *'Roxy a dormi 6h dans son panier, a bu à 3 reprises et a joué 45 minutes. Aucun signe d'anxiété ou de léthargie détecté aujourd'hui.'*")
    
    if st.button("Enregistrer les préférences Animaux"):
        st.success("Vos préférences de notifications ont été enregistrées avec succès.")
