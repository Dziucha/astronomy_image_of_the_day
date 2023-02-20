import requests
import json


def download_data(url):
    info = requests.get(url).content
    info = json.loads(info)
    return info


def save_image(image_url):
    with open("image.jpg", "wb") as file:
        image_bites = requests.get(image_url).content
        file.write(image_bites)
