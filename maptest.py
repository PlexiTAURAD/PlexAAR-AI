import requests
from pprint import pprint
import folium
import os
import streamlit as st
baseurl = 'https://nominatim.openstreetmap.org/search?format=json'

address = st.text_input('Enter your address')
if st.button("Get area map"):
    response = requests.get(f"{baseurl}&q={address}")
    data = response.json()
    latitude = data[0].get('lat')
    longitude = data[0].get('lon')
    bbox = data[0].get('boundingbox')
    location = float(latitude), float(longitude)
    map = folium.Map(location=location, width = 800, height= 400)
    st.map(map)