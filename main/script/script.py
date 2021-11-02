import requests
from main.model.train import Train
from main.utils import utils

user_dateinput = "30/12/2021"

date = utils.date_range(user_dateinput)
n = 0
minprice_list = []
train_list = []

while n < len(date):
    train_api_url2 = f"https://www.lefrecce.it/msite/api/solutions?origin=GIULIANOVA&destination=MILANO%20CENTRALE&" \
                     f"arflag=A&adate={date[n]}&atime=17&adultno=1&childno=0&direction=A&frecce=false"
    request_trains = requests.get(train_api_url2).json()  # type -> list

    for train_dict in request_trains:
        train_obj = Train(**train_dict)
        dict_train = {
            'originalPrice': train_obj.originalPrice,
            'saleable': train_obj.saleable,
            'n_changes': train_obj.changesno,
            'origin': train_obj.origin,
            'destination': train_obj.destination,
            'departuretime': train_obj.departuretime,
            'arrivaltime': train_obj.arrivaltime,
            'duration': train_obj.duration,
            'direction': train_obj.direction,
            'trains': train_obj.trainlist,
        }
        minprice_list.append(train_obj.minprice)
        train_list.append(dict_train)
    minprice_list.sort()
    utils.remove_null_values(minprice_list)

    n += 1

trlist_byprice = sorted(train_list, key=lambda d: d['originalPrice'])

# looking for saleable trains
avail_trains = []
for train in trlist_byprice:
    if not train['saleable']:
        train.clear()
    avail_trains.append(train)

    g = 0
    condit = True
    while condit:
        try:
            if len(avail_trains[g]) == 0:
                del avail_trains[g]
        except IndexError:
            condit = False
        g += 1

for a in avail_trains:
    print(a)
