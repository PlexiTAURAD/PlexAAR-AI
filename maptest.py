import requests
from pprint import pprint
import folium
import os
import streamlit as st
import cv2


baseurl = 'https://nominatim.openstreetmap.org/search?format=json'
address = "Aparna hill park, Hyderabad"
response = requests.get(f"{baseurl}&q={address}")
data = response.json()


latitude = data[0].get('lat')
longitude = data[0].get('lon')

bbox = data[0].get('boundingbox')
location = float(latitude), float(longitude)
map = folium.Map(location=location, zoom_start= 18)
folium_static = map._repr_html_()
st.components.v1.html(folium_static, width = 1080, height = 760)


image = cv2.imread("map.png")
cv2.namedWindow("Satellite Image")
cv2.imshow("Satellite Image", image)