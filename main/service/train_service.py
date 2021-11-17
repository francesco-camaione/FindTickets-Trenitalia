import grequests
from main.utils import utils


class GetTrains:
    def __init__(self, date_input):
        self.date_input = date_input

    def availables_trains(self):
        dates = utils.date_range(self.date_input)
        list_of_urls = []
        for date in dates:
            urls = f"https://www.lefrecce.it/msite/api/solutions?origin=GIULIANOVA&destination=MILANO CENTRALE&arflag=A&" \
                   f"adate={date}&atime=07&adultno=1&childno=0&direction=A&frecce=false"
            list_of_urls.append(urls)

        set_of_requests = (grequests.get(url) for url in list_of_urls)
        responses = (grequests.map(set_of_requests))  # send all requests at the same time
        json_response = [response.json() for response in responses]

        return json_response

