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

import base64
from io import BytesIO

html = folium_static.split('<body>')[1].split('</body>')[0]

html_encoded = base64.b64encode(html.encode()).decode()

html_file = f"""
<html>
<body>
<img src="data:text/html;base64,{html_encoded}">
</body>
</html>
"""

from selenium import webdriver
driver = webdriver.Chrome()
driver.get(f"data:text/html;base64,{html_encoded}")
driver.get_screenshot_as_file("map.png")
driver.quit()

image = cv2.imread("map.png")
cv2.namedWindow("Satellite Image", cv2.WINDOW_NORMAL)
cv2.imshow("Satellite Image", image)