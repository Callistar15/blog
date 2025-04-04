import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("Mon carnet de voyage")

st.markdown("### Clique sur un lieu pour explorer")

# Lieux à afficher
destinations = {
    "Singapour": {
        "lat": 1.3521,
        "lon": 103.8198
    }
}

# Création de la carte
m = folium.Map(location=[10, 20], zoom_start=2)

for nom, info in destinations.items():
    folium.Marker(
        location=[info["lat"], info["lon"]],
        popup=folium.Popup(nom, max_width=300),
        tooltip=nom
    ).add_to(m)

# Affichage de la carte et détection clic
map_data = st_folium(m, width=1000, height=600)

if map_data and map_data.get("last_object_clicked_tooltip"):
    clicked = map_data["last_object_clicked_tooltip"]
    if clicked == "Singapour":
        st.switch_page("pages/1_Singapour.py")