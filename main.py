import streamlit as st
import requests

title = st.title("title")

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/" \
      "Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg/1280px-" \
      "Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg"
image_bites = requests.get(url)

with open("image.jpg", "wb") as file:
    file.write(image_bites.content)

image = st.image("image.jpg")

description = st.text("sample description for now it is a string only")
