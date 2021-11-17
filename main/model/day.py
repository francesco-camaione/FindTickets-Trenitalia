from main.utils import utils


class Day:
    def __init__(self, data, prezzo, treni, duration):
        self.data = data
        self.prezzo = prezzo
        self.treni = treni
        self.duration = duration

    def __repr__(self):
        return f"{self.data}  {int(self.prezzo)}€  treni: {utils.train_name(self.treni)} {self.duration}h"

    def __lt__(self, other):
        return self.prezzo < other.prezzo
