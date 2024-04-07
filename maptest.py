import requests
from pprint import pprint
import folium
from streamlit_folium import st_folium
from folium.plugins import Draw
import os
import streamlit as st
import time
baseurl = 'https://nominatim.openstreetmap.org/search?format=json'

address = st.text_input('Enter your address')

response = requests.get(f"{baseurl}&q={address}")
data = response.json()
latitude = data[0].get('lat')
longitude = data[0].get('lon')
bbox = data[0].get('boundingbox')
location = float(latitude), float(longitude)
map = folium.Map(location=location, width = 1080, height= 720,zoom_start=18)
Draw(export=True).add_to(map)

c1, c2 = st.columns(2)
with c1:
    output = st_folium(map)

with c2:
    st.write(output)

st_folium(map)
    