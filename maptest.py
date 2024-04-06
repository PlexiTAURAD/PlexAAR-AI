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

circle_radius = 10
def on_mouse_event(event, x, y, flags, param):
    global image  # Make sure to use the global image variable

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), circle_radius, (0, 0, 255), 2)

        st.write(f"Clicked at ({x}, {y})")
cv2.setMouseCallback("Satellite Image", on_mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()