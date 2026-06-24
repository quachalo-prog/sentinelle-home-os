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

# Gestion du thème (Clair / Sombre)
if 'theme' not in st.session_state:
    st.session_state.theme = 'sombre'

def toggle_theme():
    st.session_state.theme = 'clair' if st.session_state.theme == 'sombre' else 'sombre'

# Application des styles CSS selon le thème
if st.session_state.theme == 'clair':
    st.markdown("""
    <style>
        .main { background-color: #f8f9fa; }
        .stApp { background-color: #f8f9fa; color: #0f172a; }
        h1, h2, h3 { color: #0f172a; font-family: 'Helvetica Neue', Arial, sans-serif; }
        .card {
            background-color: white; padding: 18px; border-radius: 12px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02); margin-bottom: 15px; border-left: 5px solid #2563eb; color: #1e293b;
        }
        .card-critical { border-left-color: #ef4444; background-color: #fef2f2; }
        .card-warning { border-left-color: #f59e0b; background-color: #fffbeb; }
        .card-info { border-left-color: #2563eb; background-color: #eff6ff; }
        .feed-time { font-size: 0.85em; color: #64748b; font-weight: bold; }
        .badge { padding: 3px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold; display: inline-block; }
        .badge-critical { background-color: #fee2e2; color: #991b1b; }
        .badge-warning { background-color: #fef3c7; color: #92400e; }
        .badge-info { background-color: #dbeafe; color: #1e40af; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        .main { background-color: #0f172a; }
        .stApp { background-color: #0f172a; color: #f1f5f9; }
        h1, h2, h3 { color: #f8fafc; font-family: 'Helvetica Neue', Arial, sans-serif; }
        .card {
            background-color: #1e293b; padding: 18px; border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2); margin-bottom: 15px; border-left: 5px solid #3b82f6; color: #e2e8f0;
        }
        .card-critical { border-left-color: #ef4444; background-color: #2d1a1a; }
        .card-warning { border-left-color: #f59e0b; background-color: #2d241a; }
        .card-info { border-left-color: #3b82f6; background-color: #1a2333; }
        .feed-time { font-size: 0.85em; color: #94a3b8; font-weight: bold; }
        .badge { padding: 3px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold; display: inline-block; }
        .badge-critical { background-color: #7f1d1d; color: #fca5a5; }
        .badge-warning { background-color: #78350f; color: #fcd34d; }
        .badge-info { background-color: #1e3a8a; color: #93c5fd; }
    </style>
    """, unsafe_allow_html=True)

# Barre latérale
st.sidebar.title("🛡️ Sentinelle Home OS")
st.sidebar.markdown("*Intelligence, Éthique & Haute Sécurité*")
st.sidebar.write("---")

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

theme_icon = "☀️ Mode Clair" if st.session_state.theme == 'sombre' else "🌙 Mode Sombre"
st.sidebar.button(theme_icon, on_click=toggle_theme)

menu = st.sidebar.radio("Navigation", ["📊 Fil narratif", "🎥 Direct & Caméras", "⚙️ Alertes & Cascade", "🐾 Paramètres Animaux"])
st.sidebar.write("---")
st.sidebar.success("● Moteur IA Cloud Connecté")

# --- ÉCRAN 1 : FIL NARRATIF ---
if menu == "📊 Fil narratif":
    st.title("📊 Fil Narratif de la Maison")
    search_query = st.text_input("🔍 Recherche sémantique (ex: 'Léo', 'Coupure')", "")
    events = [
        {"time": "14:32:08", "type": "critical", "cat": "RÉSEAU", "text": "[CRITIQUE] Perte de connexion détectée sur la 'Caméra Salon Tulear'. Raison probable : Coupure de courant.", "tag": "Alerte Système"},
        {"time": "12:15:34", "type": "warning", "cat": "ENFANTS", "text": "Léo s'est approché de la zone interdite 'Escalier'. Signal sonore local émis.", "tag": "Danger Évité"},
        {"time": "11:40:12", "type": "info", "cat": "ANIMAUX", "text": "Résumé d'activité : Le chien 'Tulear' est calme dans le salon.", "tag": "Journal de bord"}
    ]
    for e in [ev for ev in events if not search_query or search_query.lower() in ev['text'].lower()]:
        st.markdown(f"""
        <div class="card card-{e['type']}">
            <span class="feed-time">{e['time']}</span> | <span class="badge badge-{e['type']}">{e['cat']}</span>
            <div style="margin-top:7px; font-weight:500;">{e['text']}</div>
        </div>
        """, unsafe_allow_html=True)

# --- ÉCRAN 2 : DIRECT & CAMÉRAS (ACCÈS DISTANCE CLOUD) ---
elif menu == "🎥 Direct & Caméras":
    st.title("🎥 Connexion à Distance (Cloud)")
    st.markdown("Visualisez votre caméra Imou à distance grâce aux identifiants sécurisés.")
    
    col1, col2 = st.columns([1.5, 1])
    
    with col2:
        st.subheader("🔑 Identifiants Imou Cloud")
        cloud_email = st.text_input("E-mail du compte Imou", placeholder="exemple@mail.com")
        cloud_pass = st.text_input("Mot de passe du compte", type="password")
        camera_sn = st.text_input("Numéro de Série (SN)", value="7L0DFAAPAZ4610D")
        safety_code = st.text_input("Code de sécurité de l'appareil (Sous la caméra)", type="password")
        
        connect_btn = st.button("🔗 Se connecter au flux distant")
        
    with col1:
        st.subheader("Visionnage en direct")
        if connect_btn and cloud_email and cloud_pass and safety_code:
            with st.spinner("Authentification et décodage du flux sécurisé Imou..."):
                time.sleep(2)
                st.success("Connexion établie avec succès !")
                # On simule le lecteur actif connecté à la caméra
                st.video("https://assets.mixkit.co/videos/preview/mixkit-security-camera-pan-in-an-office-41551-large.mp4")
        else:
            st.info("Veuillez remplir vos identifiants à droite et cliquer sur 'Se connecter' pour afficher le flux vidéo en temps réel.")

    st.write("---")
    st.subheader("🛡️ Option Éthique (Privacy-by-Design)")
    ethique = st.checkbox("Activer le rendu Squelette 3D (Masque l'image brute pour protéger l'intimité)", value=False)
    if ethique:
        st.warning("Mode Éthique activé : L'image réelle est floutée, seuls les mouvements suspects sont analysés.")

# --- ÉCRAN 3 & 4 (STABLES) ---
elif menu == "⚙️ Alertes & Cascade":
    st.title("⚙️ Sécurité Critique")
    if st.button("🚨 Déclencher une simulation de panne réseau"):
        st.error(f"🚨 ALERT SYSTÈME à {datetime.now().strftime('%H:%M:%S')} — Perte de signal sur 'Salon Tulear'.")
elif menu == "🐾 Paramètres Animaux":
    st.title("🐾 Paramètres Animaux")
    st.radio("Mode de notification :", ["📱 Mode Live Tracker (Direct)", "📅 Mode Journal de Bord (Résumé)"])
