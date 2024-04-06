import requests
from pprint import pprint
import folium
import os
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

baseurl = 'https://nominatim.openstreetmap.org/search?format=json'
address = "Aparna hill park, Hyderabad"
response = requests.get(f"{baseurl}&q={address}")
data = response.json()
latitude = data[0].get('lat')
longitude = data[0].get('lon')
bbox = data[0].get('boundingbox')
location = float(latitude), float(longitude)

map = folium.Map(location=location, zoom_start=18)
folium_static = map._repr_html_()
st.components.v1.html(folium_static, width=1080, height=760)

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

circle_radius = 10

def on_mouse_event(event, x, y, flags, param):
    global image  

    if event == cv2.EVENT_LBUTTONDOWN:
       
        cv2.circle(image, (x, y), circle_radius, (0, 0, 255), 2)

        cv2.imshow("Satellite Image", image)

        st.write(f"Clicked at ({x}, {y})")

cv2.setMouseCallback("Satellite Image", on_mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()