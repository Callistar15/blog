import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("Mon carnet de voyage 🌍")

st.markdown("### Clique sur un lieu pour explorer")

destinations = {
    "Singapour": {
        "lat": 1.3521,
        "lon": 103.8198
    }
}

m = folium.Map(location=[10, 20], zoom_start=2)

for nom, info in destinations.items():
    folium.Marker(
        location=[info["lat"], info["lon"]],
        popup=folium.Popup(nom, max_width=300),
        tooltip=nom
    ).add_to(m)

st_folium(m, width=1000, height=600)

st.markdown("🔍 Ensuite, clique dans le menu à gauche pour découvrir chaque destination !")
