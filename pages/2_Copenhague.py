import streamlit as st
from streamlit.components.v1 import html
import os

# === TITRE ===
st.title("Copenhague")
st.subheader("🌍 LA ville Scandinave")

# === SECTIONS DÉROULANTES ===
st.markdown("### 📌 À découvrir")

from streamlit_folium import st_folium
import folium

with st.expander("🍳 Les meilleurs Brunch de la ville"):

    st.markdown("""
**[Atelier Septembre](https://cafeatelierseptember.com/)** – 🎡 L'un des meilleurs brunch de Copenhague - 🍳 Brunch à Copenhague
📍 Situé dans le quartier de Nørrebro, super central et facile d’accès
🥑 Carte canon : avocado toast, shakshuka, pancakes… tout est fait maison
💸 Prix doux pour CPH – plats entre 90 et 150 DKK
🎶 Petite touche de musique électronique chill en fond, ambiance locale & décontractée
👩‍🎓 Spot apprécié des jeunes & étudiants – parfait pour un dimanche tranquille entre potes

---

**[Det Vide Hus](https://www.tripadvisor.fr/Restaurant_Review-g189541-d6974756-Reviews-Cafe_Det_Vide_Hus-Copenhagen_Zealand.html)** - 🍽 Brunch à Copenhague
📍 Niché dans Vesterbro, un coin cool et arty
🍳 Cuisine créative & locale : brunch nordique revisité, pain maison, œufs bio, etc.
💸 Un peu plus haut de gamme – compte 150 à 200 DKK par personne
🌿 Déco épurée, vibe scandi-minimaliste, parfait pour les brunchs posés
🎶 Ambiance calme, pas de musique forte, juste le bruit des fourchettes et du café qui coule ☕

---

**[Seks](https://www.sekscph.com/)** - 🍽 Brunch à Copenhague
📍 En plein centre-ville, à deux pas de Strøget – super pratique
🍳 Menu fusion scandi / latino : huevos rancheros, toasts colorés, options végé/végan
💸 Très raisonnable pour l’emplacement – entre 80 et 140 DKK le plat
🎨 Ambiance arty & cozy, murs colorés et staff super friendly
🎶 Petit fond de musique chill, parfait pour un brunch détente ou un café solo
    """)

# === MINI CARTE INTERACTIVE ===
st.markdown("#### 🗺 Localisation des lieux")

lieux_sortie = {
    # Quartier de l'Université – Bars
    "Café Bastard": {
        "lat": 55.6780,
        "lon": 12.5740,
        "desc": "Bar à jeux très convoité 🎲 snacks et boissons",
        "address": "Rådhusstræde 13, 1466 København K, Denmark"
    },
    "Bar' Godt": {
        "lat": 55.6790,
        "lon": 12.5750,
        "desc": "Petit bar cosy populaire auprès des étudiants 🍻",
        "address": "Kejsergade 1, 1155 København K, Denmark"
    },
    "Luke's Bar": {
        "lat": 55.6800,
        "lon": 12.5760,
        "desc": "Ambiance étudiante et prix doux 🎓",
        "address": "Klosterstræde 23, 1157 København K, Denmark"
    },
    "Vesper Bar": {
        "lat": 55.6810,
        "lon": 12.5770,
        "desc": "Cocktails raffinés dans une ambiance chill 🍸",
        "address": "Kompagnistræde 9, 1208 København K, Denmark"
    },
    "Bar Somm'": {
        "lat": 55.6820,
        "lon": 12.5780,
        "desc": "Bar à vin moderne & décontracté 🍷",
        "address": "Vendersgade 10, 1363 København K, Denmark"
    },

    # Quartier Vesterbro/Kongens Enghave
    "Kødbyen": {
        "lat": 55.6700,
        "lon": 12.5500,
        "desc": "Zone branchée avec bars et restos étudiants 🍔🍺",
        "address": "Flæsketorvet, 1711 København V, Denmark"
    },

    # Brunch spots
    "Atelier September": {
        "lat": 55.6830,
        "lon": 12.5805,
        "desc": "Brunch local & chill à Nørrebro 🍳",
        "address": "Kronprinsessegade 62, 1306 København K, Denmark"
    },
    "Det Vide Hus": {
        "lat": 55.6840,
        "lon": 12.5815,
        "desc": "Cuisine nordique créative à Vesterbro 🌿",
        "address": "Gothersgade 113, 1123 København K, Denmark"
    },
    "Seks": {
        "lat": 55.6850,
        "lon": 12.5825,
        "desc": "Brunch scandi-latino au cœur du centre-ville 🌈",
        "address": "Krystalgade 6, 1172 København K, Denmark"
    }
}

# Affichage de la carte
m = folium.Map(location=[55.678, 12.57], zoom_start=13)

for nom, info in lieux_sortie.items():
    folium.Marker(
        location=[info["lat"], info["lon"]],
        popup=f"<b>{nom}</b><br>{info['desc']}<br>{info['address']}",
        tooltip=nom,
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

st_folium(m, height=400, width=800)

    
with st.expander("🍸 Prendre un verre"):
    st.write("Essayez les rooftops comme SKT. Petri ou Illum Rooftop. Pour une ambiance plus intime, direction un bar à vin à Vesterbro.")

with st.expander("🍽 Brunchs & cafés"):
    st.write("Incontournables : Brunch Atelier à Nørrebro, Seks en centre-ville, ou Det Vide Hus à Vesterbro. Carte créative, vibes locales.")

with st.expander("🌆 Balades urbaines"):
    st.write("Explorez Nyhavn, flânez le long des canaux, ou perdez-vous dans les rues de Christianshavn. Parfait en vélo ou à pied.")

with st.expander("🚲 À faire comme un local"):
    st.write("Louer un vélo est quasi obligatoire. Copenhague est l'une des meilleures villes cyclables du monde.")

with st.expander("🎨 Culture & musées"):
    st.write("Louisiana Museum un peu en dehors de la ville est magique. Sinon, ne manquez pas la Glyptotek ou le Designmuseum.")

with st.expander("💡 Bons plans"):
    st.write("La Copenhagen Card donne accès aux musées + transports. Pensez aussi aux boulangeries locales pour un dej à petit prix.")
    
with st.expander("🌈 Christiania – quartier alternatif"):
    st.write("Autoproclamée ville libre, *Christiania* est un incontournable. Street art, cafés atypiques, esprit communautaire… Un endroit à part, très chill, à découvrir avec respect.")
    
st.markdown("---")



# === MUSIQUE ===
st.markdown("### 🎧 Ambiance musicale – Goodbyes de Post Malone")

html("""
<iframe width="100%" height="315" src="https://www.youtube.com/embed/ba7mB8oueCY"
frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
""", height=315)


# === RETOUR À LA CARTE ===
st.markdown("[← Retour à la carte](../Accueil)")