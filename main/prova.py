import grequests
from main import calendar_bestprices
from service.train_service import availabl_trains

response = availabl_trains('Giulianova', 'Lecce', '01/02/2022', 1, 0, '07')
calend_prices = calendar_bestprices(response)
print(calend_prices)
