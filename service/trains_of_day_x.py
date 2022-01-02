import grequests


class Tr_Dayx:

    def __init__(self, origin, destination, day, month, year, n_adult, n_baby):
        self.origin = origin
        self.destination = destination
        self.day = day
        self.month = month
        self.year = year
        self.n_adult = n_adult
        self.n_baby = n_baby
        self.date = f"{day}/{month}/{year}"

    def get_data(self):
        hhs = ["06", "07", "08", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        list_of_urls = []
        for hh in hhs:
            url = f"https://www.lefrecce.it/msite/api/solutions?origin={self.origin}&destination={self.destination}" \
                  f"&arflag=A&adate={self.date}&atime={hh}&adultno={self.n_adult}" \
                  f"&childno={self.n_baby}&direction=A&frecce=false"
            list_of_urls.append(url)

        set_of_requests = (grequests.get(url) for url in list_of_urls)
        responses = (grequests.map(set_of_requests))
        json_response = []
        for response in responses:
            if response is not None:
                json_response.append(response.json())
            if response is None:
                json_response.append("")
        return json_response
