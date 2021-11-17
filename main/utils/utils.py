from datetime import timedelta, datetime


def date_range(date_input):
    date = datetime.strptime(date_input, "%d/%m/%Y").date()
    newdate = []
    for i in range(0, 30):
        newdate.append(str((date + timedelta(days=i)).strftime("%d/%m/%Y")))
    return newdate


def get_time(iso_date: int):
    time_ = datetime.utcfromtimestamp(iso_date / 1000).strftime('%H:%M')
    return time_


def get_date(iso_date: int):
    date_ = datetime.utcfromtimestamp(iso_date / 1000).strftime('%d-%m-%Y')
    return date_


def train_name(trainlist: list):
    names = [treni_["trainidentifier"] for treni_ in trainlist]
    train_names = ""
    if len(names) >= 3:
        train_names += f"{names[0]}; {names[1]}; {names[2]}"
    if len(names) == 2:
        train_names += f"{names[0]}; {names[1]}"
    if len(names) == 1:
        train_names += f"{names[0]}"
    return train_names
