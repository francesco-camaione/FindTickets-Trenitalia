from utils import utils
import grequests


def availabl_trains(origin, destination, data, n_adult, n_baby, atime):
    dates = utils.date_range(data)
    list_of_urls = []
    for date in dates:
        urls = f"https://www.lefrecce.it/msite/api/solutions?origin={origin}&destination={destination}&arflag=A&" \
               f"adate={date}&atime={atime}&adultno={n_adult}&childno={n_baby}&direction=A&frecce=false"
        list_of_urls.append(urls)

    set_of_requests = (grequests.get(url) for url in list_of_urls)
    responses = (grequests.map(set_of_requests))  # send all requests at the same time

    json_response = [response.json() for response in responses if response.status_code == 200]
    return json_response
