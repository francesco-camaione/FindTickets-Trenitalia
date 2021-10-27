import requests
from fastapi import FastAPI

app = FastAPI()

train_api_url = "https://www.lefrecce.it/msite/api/solutions?origin=GIULIANOVA&destination=MILANO%20CENTRALE&arflag=A&"\
                "adate=27/10/2021&atime=17&adultno=1&childno=0&direction=A&frecce=false&onlyRegional=true"


@app.get("/")
def x():
    request_trains = requests.get(train_api_url)
    return request_trains.json()
