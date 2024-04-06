import requests
import folium
import streamlit as st
import cv2
import numpy as np

baseurl = 'https://nominatim.openstreetmap.org/search?format=json'
address = "Aparna hill park, Hyderabad"
response = requests.get(f"{baseurl}&q={address}")
data = response.json()
latitude = data[0].get('lat')
longitude = data[0].get('lon')
bbox = [float(x) for x in data[0].get('boundingbox')]
location = float(latitude), float(longitude)

map = folium.Map(location=location, zoom_start=18)
folium_static = map._repr_html_()
st.components.v1.html(folium_static, height=500, width=700)

# Fetch and stitch satellite image tiles
tiles = []
for x in range(int(bbox[2]), int(bbox[3]) + 1):
    row = []
    for y in range(int(bbox[0]), int(bbox[1]) + 1):
        tile_url = f"https://tile.openstreetmap.org/18/{x}/{y}.png"
        response = requests.get(tile_url)
        if response.status_code == 200:
            tile = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
            row.append(tile)
    tiles.append(cv2.hconcat(row))

stitched_image = cv2.vconcat(tiles)

circle_radius = 10

def process_image(stitched_image, x, y):
    if stitched_image is not None and 0 <= x < stitched_image.shape[1] and 0 <= y < stitched_image.shape[0]:
        cv2.circle(stitched_image, (x, y), circle_radius, (0, 0, 255), 2)
    return stitched_image

def on_map_click(coords):
    x, y = coords
    processed_image = process_image(stitched_image.copy(), int(x), int(y))
    if processed_image is not None:
        st.image(processed_image, channels="BGR")

map.add_child(folium.ClickEventHandler(callback=on_map_click))

st.subheader("Click on the map to add a circle")