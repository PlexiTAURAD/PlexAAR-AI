import requests
from pprint import pprint
import folium
from streamlit_folium import st_folium
from folium.plugins import Draw
import os
import streamlit as st
import time
from geopy.distance import distance

baseurl = 'https://nominatim.openstreetmap.org/search?format=json'

address = st.text_input('Enter your address')
response = requests.get(f"{baseurl}&q={address}")
data = response.json()
latitude = data[0].get('lat')
longitude = data[0].get('lon')
bbox = data[0].get('boundingbox')
location = float(latitude), float(longitude)
map = folium.Map(location=location, width = 1080, height= 720,zoom_start=3)

bank1 = float(13.04059886932373), float(77.61155700683594) # Food bank
bank2 = float(13.009804), float(77.3991149) # Feed India
bank3 = float(12.9532653), float(77.4914687) # The public fridge

km1 = distance(location,bank1)
km2 = distance(location,bank2)
km3 = distance(location,bank3)
wat = min(km1,km2,km3)

folium.Marker(location=bank1, popup="Food bank").add_to(map)
folium.Marker(location=bank2, popup="Feed India").add_to(map)
folium.Marker(location=bank3, popup="The public fridge").add_to(map)

if wat == km1:
    folium.PolyLine((location,bank1)).add_to(map)
elif wat == km2:
    folium.PolyLine((location,bank2)).add_to(map)
else:
    folium.PolyLine((location,bank3)).add_to(map)

st_folium(map)
