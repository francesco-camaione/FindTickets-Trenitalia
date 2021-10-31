import requests
from main.model.train import Train
from main.utils import utils

user_dateinput = input("enter date in DD/MM/YYYY: ")

date = utils.date_range(user_dateinput)
n = 0
prices = []
minprice_list = []
saleable_list = []
while n < len(date):
    train_api_url2 = f"https://www.lefrecce.it/msite/api/solutions?origin=GIULIANOVA&destination=MILANO%20CENTRALE&" \
                     f"arflag=A&adate={date[n]}&atime=17&adultno=1&childno=0&direction=A&frecce=false"
    request_trains = requests.get(train_api_url2).json()  # type -> list
    g = 0
    k = 0

    for train_dict in request_trains:
        train_obj = Train(**train_dict)
        minprice_list.append(train_obj.minprice)
        saleable_list.append(train_obj.saleable)

    minprice_list.sort()
    prices.append(utils.remove_null_values(minprice_list))
    n += 1


print(minprice_list[0])

#  ora devo ritrovare le caratteristiche del treno a quel prezzo
