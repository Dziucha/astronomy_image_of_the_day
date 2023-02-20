import streamlit as st
import functions
# import requests

api = "kUMVV5bF43mbXI6kIRbPMiEhFcjyEABHaSBQ0HCS"
url = f"https://api.nasa.gov/planetary/apod?api_key={api}"
image_of_the_day = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/2560px-Cat_August_2010-4.jpg"

data = functions.download_data(url)

title = st.title(data["title"].title())

picture_url = data["url"]
functions.save_image(picture_url)

image = st.image("image.jpg")

description = st.info(data["explanation"])
