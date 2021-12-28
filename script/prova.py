import requests


def stations(letters: str):
    res = requests.get("https://www.lefrecce.it/msite/api/geolocations/locations?name=" + letters)
    return res.json()
