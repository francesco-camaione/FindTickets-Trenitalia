from utils import utils


class Day:
    def __init__(self, date, price, trains, duration):
        self.date = date
        self.price = price
        self.trains = trains
        self.duration = duration

    def __repr__(self):
        return f"{self.date}  {int(self.price)}  treni: {utils.train_name(self.trains)} {self.duration}h"
