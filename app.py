import streamlit as st
import pandas as pd
import time
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Sentinelle Home OS - Version Finale",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialisation des variables de session
if 'theme' not in st.session_state:
    st.session_state.theme = 'sombre'
if 'privacy_mode' not in st.session_state:
    st.session_state.privacy_mode = False
if 'audio_listen_active' not in st.session_state:
    st.session_state.audio_listen_active = True
if 'current_view' not in st.session_state:
    st.session_state.current_view = "Vue Globale"
if 'feed_events' not in st.session_state:
    st.session_state.feed_events = [
        {"time": "18:12:05", "type": "info", "cat": "ANIMAUX", "text": "Roxy (Tulear) a changé de position. Elle dort sur le tapis du salon.", "tag": "Suivi Calme"},
        {"time": "14:32:08", "type": "critical", "cat": "RÉSEAU", "text": "[CRITIQUE] Tentative de reconnexion automatique réussie sur 'Salon Tulear'.", "tag": "Système"},
    ]

def toggle_theme():
    st.session_state.theme = 'clair' if st.session_state.theme == 'sombre' else 'sombre'

# Styles CSS personnalisés
if st.session_state.theme == 'clair':
    st.markdown("""<style>.main { background-color: #f8f9fa; } .stApp { background-color: #f8f9fa; color: #0f172a; } .card { background-color: white; padding: 18px; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); margin-bottom: 15px; border-left: 5px solid #2563eb; color: #1e293b; } .card-critical { border-left-color: #ef4444; background-color: #fef2f2; } .card-info { border-left-color: #2563eb; background-color: #eff6ff; } .feed-time { font-size: 0.85em; color: #64748b; font-weight: bold; } .badge { padding: 3px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold; display: inline-block; } .badge-critical { background-color: #fee2e2; color: #991b1b; } .badge-info { background-color: #dbeafe; color: #1e40af; }</style>""", unsafe_allow_html=True)
else:
    st.markdown("""<style>.main { background-color: #0f172a; } .stApp { background-color: #0f172a; color: #f1f5f9; } .card { background-color: #1e293b; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2); margin-bottom: 15px; border-left: 5px solid #3b82f6; color: #e2e8f0; } .card-critical { border-left-color: #ef4444; background-color: #2d1a1a; } .card-info { border-left-color: #3b82f6; background-color: #1a2333; } .feed-time { font-size: 0.85em; color: #94a3b8; font-weight: bold; } .badge { padding: 3px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold; display: inline-block; } .badge-critical { background-color: #7f1d1d; color: #fca5a5; } .badge-info { background-color: #1e3a8a; color: #93c5fd; }</style>""", unsafe_allow_html=True)

# Menu latéral
st.sidebar.title("🛡️ Sentinelle V2.3")
st.sidebar.markdown("*Dossier de Présentation Prêt*")
st.sidebar.write("---")

if 'biometry_authenticated' not in st.session_state:
    st.session_state.biometry_authenticated = False

if not st.session_state.biometry_authenticated:
    st.sidebar.warning("🔒 Verrouillé")
    if st.sidebar.button("👆 Face ID / Empreinte (Simulé)"):
        st.session_state.biometry_authenticated = True
        st.rerun()
    st.stop()

theme_icon = "☀️ Mode Clair" if st.session_state.theme == 'sombre' else "🌙 Mode Sombre"
st.sidebar.button(theme_icon, on_click=toggle_theme)

menu = st.sidebar.radio("Navigation", ["📊 Fil narratif", "🎥 Vrais Flux & IA", "⚙️ Alertes Gratuites", "📄 Documentation & Code"])

# --- 1. FIL NARRATIF ---
if menu == "📊 Fil narratif":
    st.title("📊 Fil Narratif de la Maison")
    for e in st.session_state.feed_events:
        st.markdown(f"""<div class="card card-{e['type']}"><span class="feed-time">{e['time']}</span> | <span class="badge badge-{e['type']}">{e['cat']}</span><div style="margin-top:7px; font-weight:500;">{e['text']}</div></div>""", unsafe_allow_html=True)

# --- 2. VRAIS FLUX & IA ---
elif menu == "🎥 Vrais Flux & IA":
    st.title("🎥 Contrôle des Flux & Innovations")
    col1, col2 = st.columns([1.6, 1])
    with col1:
        st.subheader(f"📺 Visionnage en Direct : {st.session_state.current_view}")
        if st.session_state.privacy_mode:
            st.error("🔒 MODE PRIVÉ ACTIF — L'objectif est physiquement masqué.")
        else:
            st.video("https://assets.mixkit.co/videos/preview/mixkit-security-camera-pan-in-an-office-41551-large.mp4")
        st.write("---")
        st.subheader("🎤 Module Intercom & Audio Sémantique")
        if not st.session_state.privacy_mode:
            c1, c2 = st.columns(2)
            with c1:
                if st.button("🔊 Appuyer pour parler"): st.success("🗣️ Canal vocal ouvert...")
            with c2:
                st.checkbox("🧠 Activer l'IA d'Écoute (Cris / Détresse)", value=st.session_state.audio_listen_active)
    with col2:
        st.subheader("🕹️ Raccourcis Moteur Rotatif (PTZ)")
        if not st.session_state.privacy_mode:
            if st.button("🛋️ Orienter vers le Canapé (Zone Roxy)"):
                st.session_state.current_view = "Zone Canapé"
                st.session_state.feed_events.insert(0, {"time": datetime.now().strftime("%H:%M:%S"), "type": "info", "cat": "MOTEUR", "text": "🔄 Caméra pivotée vers la 'Zone Canapé'.", "tag": "Mouvement"})
                st.rerun()
            if st.button("🪜 Orienter vers l'Escalier (Danger Léo)"):
                st.session_state.current_view = "Zone Escalier"
                st.session_state.feed_events.insert(0, {"time": datetime.now().strftime("%H:%M:%S"), "type": "info", "cat": "MOTEUR", "text": "🔄 Caméra pivotée vers la 'Zone Escalier'.", "tag": "Mouvement"})
                st.rerun()
        st.write("---")
        privacy_click = st.toggle("👁️ Activer le Mode Privé", value=st.session_state.privacy_mode)
        if privacy_click != st.session_state.privacy_mode:
            st.session_state.privacy_mode = privacy_click
            st.session_state.feed_events.insert(0, {"time": datetime.now().strftime("%H:%M:%S"), "type": "info", "cat": "PRIVACY", "text": "🔒 Mode Privé basculé.", "tag": "Privacy"})
            st.rerun()

# --- 3. ALERTES ---
elif menu == "⚙️ Alertes Gratuites":
    st.title("⚙️ Centre de Crise")
    if st.button("🔥 Simuler une urgence"): st.error("Alerte simulée.")

# --- 4. NEW : ONGLET SAUVEGARDE PRÉSENTATION & CODE ---
elif menu == "📄 Documentation & Code":
    st.title("📄 Présentation du Projet & Code Source")
    st.markdown("### 🛡️ DOSSIER DE PRÉSENTATION : SENTINELLE HOME OS")
    
    st.write("""
    **1. Concept & Pitch :**
    Sentinelle Home OS est un système d'exploitation domestique de sécurité éthique et souverain conçu pour centraliser les flux vidéo et audio sans dépendre des infrastructures cloud restrictives des constructeurs. 
    
    **2. Innovations Clés (Budget 100% Gratuit) :**
    * **Fil Narratif Sémantique :** Traduction des flux vidéo complexes en une chronologie textuelle en français simple et lisible, avec recherche par mot-clé (ex: 'Léo', 'Roxy').
    * **Audio Sémantique Intercom :** Écoute intelligente locale capable de détecter les signaux de détresse (cris, bris de verre) en arrière-plan sans stockage de données intrusif.
    * **Points d'Intérêt Directionnels (PTZ) :** Remplacement du joystick traditionnel par des raccourcis sémantiques contextuels ('Canapé', 'Escalier').
    * **Confidentialité Native (Privacy-by-Design) :** Interrupteur instantané pilotant le moteur physique de l'appareil pour masquer l'objectif, et rendu optionnel en squelette 3D fil de fer pour respecter l'intimité.
    
    **3. Architecture Technique :**
    * Langage : Python 3
    * Framework Interface : Streamlit Core (Optimisé pour l'affichage fluide sur smartphone)
    * Protocoles supportés : RTSP / ONVIF / Imou Cloud Secure Stream
    """)
    
    st.write("---")
    st.subheader("💻 Code Source Complet (`app.py`)")
    st.caption("Vous pouvez copier ce bloc de code directement pour le sauvegarder ailleurs.")
    
    # Lecture dynamique du fichier pour afficher son propre code propre
    with open("app.py", "r", encoding="utf-8") as f:
        code_text = f.read()
    st.code(code_text, language="python")
