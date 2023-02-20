import requests
import json

# api = "kUMVV5bF43mbXI6kIRbPMiEhFcjyEABHaSBQ0HCS"
# url = f"https://api.nasa.gov/planetary/apod?api_key={api}"


def download_data(url):
    info = requests.get(url).content
    info = json.loads(info)
    return info


def save_image(image_url):
    with open("image.jpg", "wb") as file:
        file.write(image_url)
