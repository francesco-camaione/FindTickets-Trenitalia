import requests

from main.model.train import Train
from utils import utils

train_api_url = "https://www.lefrecce.it/msite/api/solutions?origin=GIULIANOVA&destination=MILANO%20CENTRALE&arflag=A" \
                "&adate=20/11/2021&atime=17&adultno=1&childno=0&direction=A&frecce=false"

request_trains = requests.get(train_api_url).json()  # type -> list

minprice_list = []
saleable_list = []
for train_dict in request_trains:
    train_obj = Train(**train_dict)
    minprice_list.append(train_obj.minprice)
    saleable_list.append(train_obj.saleable)

minprice_list.sort()
print(utils.remove_null_values(minprice_list))

# ora bisogna cercare tramite l'url i prezzi minori del primo in minprice_list con una varianza di 2 o 3 settimane
