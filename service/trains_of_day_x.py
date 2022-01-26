import grequests


class Tr_Dayx:

    def __init__(self, origin, destination, day, month, year, n_adult, n_baby, atime, frecce):
        self.origin = origin
        self.destination = destination
        self.day = day
        self.month = month
        self.year = year
        self.n_adult = n_adult
        self.n_baby = n_baby
        self.date = f"{day}/{month}/{year}"
        self.atime = atime
        self.frecce = frecce

    def get_data(self):
        hhs = [self.atime, "11", "15", "18"]
        list_of_urls = []
        for hh in hhs:
            url = f"https://www.lefrecce.it/msite/api/solutions?origin={self.origin}&destination={self.destination}" \
                  f"&arflag=A&adate={self.date}&atime={hh}&adultno={self.n_adult}" \
                  f"&childno={self.n_baby}&direction=A&frecce={self.frecce}&onlyRegional=false"
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
