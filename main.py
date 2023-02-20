import streamlit as st
import functions

api = "kUMVV5bF43mbXI6kIRbPMiEhFcjyEABHaSBQ0HCS"
url = f"https://api.nasa.gov/planetary/apod?apikey={api}"
image_of_the_day = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/2560px-Cat_August_2010-4.jpg"

title = st.title("title")

data = functions.download_data(url)
# picture_url = data["url"]

# data_frame = functions.extract_data()

# image = st.image("image.jpg")

description = st.text("sample description for now it is a string only")