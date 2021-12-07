from datetime import datetime


def get_time(iso_date: int):
    time_ = datetime.utcfromtimestamp(iso_date / 1000).strftime('%H:%M')
    return time_


iso = 1640701200000

print(get_time(iso))
