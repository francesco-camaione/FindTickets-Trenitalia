from main.utils import utils

a = [{"trainidentifier":"FRECCIARGENTO 8806","trainacronym":"FA","traintype":"F","pricetype":"D"},
     {"trainidentifier":"FRECCIAROSSA 9512","trainacronym":"FR","traintype":"F","pricetype":"D"}]
false = [{"trainidentifier":"Intercity 604","trainacronym":"IC","traintype":"T","pricetype":"D"},
         {"trainidentifier":"FRECCIAROSSA 9522","trainacronym":"FR","traintype":"F","pricetype":"D"}]
c = utils.train_name(false)
print(c)