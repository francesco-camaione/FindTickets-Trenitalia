from datetime import timedelta, datetime


def remove_null_values(lst: list):
    i = 0
    while 0 in lst:
        lst.remove(0)
    i += 1
    return lst


def date_range(date_input):
    date = datetime.strptime(date_input, "%d/%m/%Y").date()
    i = -1
    newdate = []

    while i < 15:
        newdate.append(str((date + timedelta(days=i)).strftime("%d/%m/%Y")))
        i += 1

    return newdate
