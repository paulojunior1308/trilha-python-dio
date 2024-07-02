from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours= -3)))

print(data_oslo)
print(data_sao_paulo)

##### EXEMPLO DE CÓDIGO #####
#import datetime
#
## Criando datetime com timezone
#d = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3), "BRT"))
#print(d) # 2024-07-02 16:24:10.004791-03:00
#
## Convertendo para outro timezone
#d_utc = d.astimezone(datetime.timezone.utc)
#print(d_utc) # 2024-07-02 19:24:10.004791+00:00