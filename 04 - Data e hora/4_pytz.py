import pytz
from datetime import datetime

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)




##### EXEMPLO DE CÓDIGO #####
#
## pip install pytz
#import datetime
#import pytz
#
## Criando datetime com timezone
#d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
#print(d)