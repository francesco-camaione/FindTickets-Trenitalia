from utils import utils
import grequests


def availabl_trains(origin, destination, data, n_adult, n_baby, atime, frecce):
    dates = utils.date_range(data)  # process month dates
    list_of_urls = []
    for date in dates:
        urls = f"https://www.lefrecce.it/msite/api/solutions?origin={origin}&destination={destination}&arflag=A&" \
               f"adate={date}&atime={atime}&adultno={n_adult}&childno={n_baby}&direction=A&frecce={frecce}" \
               f"&onlyRegional=false"
        list_of_urls.append(urls)

    set_of_requests = (grequests.get(url, timeout=6.00, stream=True) for url in list_of_urls)
    responses = grequests.map(set_of_requests)  # send requests at the same time
    json_response = []
    for response in responses:
        if response is not None:
            json_response.append(response.json())
        if response is None:
            json_response.append("")
    return json_response
