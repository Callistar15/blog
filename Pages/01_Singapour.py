import streamlit as st
from streamlit.components.v1 import html
import os

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# === TITRE ===
st.title("Singapour")
st.subheader("🌍 Ma ville d’échange de août à décembre 2023")

# === GALERIE DE PHOTOS EN GRILLE ===
st.markdown("### 📸 Quelques images de l’aventure")

# Dossier contenant les images JPEG
image_dir = "images"
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith((".jpg", ".jpeg"))]

# Afficher les images par rangées de 3
for i in range(0, len(image_files), 3):
    cols = st.columns(3)
    for col_index, img_index in enumerate(range(i, min(i+3, len(image_files)))):
        with cols[col_index]:
            img_path = os.path.join(image_dir, image_files[img_index])
            st.image(img_path, use_container_width=True)
            st.caption(f"📷 {image_files[img_index]}")


# Dossier contenant les images JPEG
image_dir = "images"
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith((".jpg", ".jpeg"))]


# === SECTIONS DÉROULANTES ===
st.markdown("### 📌 À découvrir")

from streamlit_folium import st_folium
import folium

with st.expander("🎭 Sortir à Singapour"):

    st.markdown("""
**[CÉ LA VI](https://www.celavi.com/en/singapore/)** – 🏙️ *Rooftop de Marina Bay Sands*  
Bar/club très international avec une vue magnifique sur Singapour.  
🎉 Mercredi = **Ladies' Night** → entrée gratuite pour les filles  
🎓 Fréquenté par les étudiants en échange (SMU, NUS, ESSEC)  
🕛 Entrer **avant minuit** et **avoir +21 ans**  
🛑 *Éviter de froisser les vigiles, ils peuvent être stricts*

---

**[Marquee Singapore](https://marqueesingapore.com/)** – 🎡 *Boîte de nuit dans The Shoppes at Marina Bay Sands*  
Club immense avec une grande roue et toboggan à l'intérieur 😮  
🎶 Musique électronique / tech, plus de locaux, ambiance jeune  
🔥 Top quand des **DJ connus** passent  
🎓 Entrées gratuites parfois pour les étudiants – à surveiller !

---

**[Jungle Ballroom](https://www.cntraveller.com/gallery/singapore-new-bars)** – 🍸 *Bar dansant à Chinatown*  
Ambiance fancy, musique house, clientèle plus âgée  
💃 Entrée gratuite  
⏰ Ferme vers 2h

---

**Le rooftop des Français 🇫🇷**  
Lieu non-officiel mais très connu dans la communauté étudiante française  
👨‍🎓 Organisé régulièrement par des étudiants (ESSEC surtout)  
📦 La coloc se transmet d’année en année → **demander autour de toi**

---

**[Avenue Lounge](https://avenuesingapore.com/)** – 🛋️ *Lounge élégant à Marina Bay Sands*  
Ambiance plus chic, clientèle plus âgée  
⚠️ Avoir **21+ ans**  
🙈 *Pas encore testé mais les retours sont bons !*
    """)

    # === MINI CARTE INTERACTIVE ===
    st.markdown("#### 🗺️ Localisation des lieux")

    lieux_sortie = {
        "CÉ LA VI": {
            "lat": 1.2834,
            "lon": 103.8607,
            "desc": "Rooftop de Marina Bay – vue panoramique. 🎉"
        },
        "Marquee": {
            "lat": 1.2833,
            "lon": 103.8600,
            "desc": "Club géant avec grande roue 🎡 musique tech"
        },
        "Jungle Ballroom": {
            "lat": 1.2805,
            "lon": 103.8456,
            "desc": "Bar dansant à Chinatown 🎶"
        },
        "Avenue Lounge": {
            "lat": 1.2836,
            "lon": 103.8605,
            "desc": "Lounge chic à Marina Bay 🛋️"
        },
        "Rooftop des Français": {
            "lat": 1.2825,
            "lon": 103.8520,
            "desc": "Coloc française non-officielle 🇫🇷"
        }
    }

    m = folium.Map(location=[1.283, 103.85], zoom_start=14)

    for nom, info in lieux_sortie.items():
        folium.Marker(
            location=[info["lat"], info["lon"]],
            popup=f"<b>{nom}</b><br>{info['desc']}",
            tooltip=nom,
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    st_folium(m, height=400, width=800)

    
with st.expander("🍸 Prendre un verre"):
    st.write("Essayez le 'Smoke & Mirrors' pour la vue sur Marina Bay, ou un speakeasy caché dans Haji Lane.")

with st.expander("🍜 Restaurants"):
    st.write("Hawker Centers pour manger comme un roi à 3€. Maxwell Food Centre est un must.")

with st.expander("🌃 Balades nocturnes"):
    st.write("La promenade autour de Marina Bay est magique de nuit. Bonus : c’est climatisé naturellement par le vent !")

with st.expander("🥾 Randonnée"):
    st.write("MacRitchie Reservoir et sa canopée suspendue : nature et varans au programme.")

with st.expander("🏁 F1 à Singapour"):
    st.write("L’unique Grand Prix de nuit au monde – à vivre au moins une fois dans sa vie. Frissons garantis.")

with st.expander("💡 Bons plans"):
    st.write("La EZ-Link card pour le métro, les apps locales comme Grab pour se déplacer, et des happy hours à repérer !")

st.markdown("---")

# === MUSIQUE ===
st.markdown("### 🎧 Ambiance musicale – *Goodbyes* de Post Malone")

html("""
<iframe width="100%" height="315" src="https://www.youtube.com/embed/ba7mB8oueCY"
frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
""", height=315)


# === RETOUR À LA CARTE ===
st.markdown("[← Retour à la carte](../Accueil)")
