from datetime import timedelta, datetime


tipo_carro = 'M' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()


if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')




##### EXEMPLO DE CÓDIGO #####
#import datetime
#
## Criando data e hora
#d = datetime.datetime(2023, 7, 19, 13, 45)
#print(d) # 2023-07-19 13:45:00
#
## Adicionando uma semana
#d = d + datetime.timedelta(weeks=1)
#print(d) # 2023-07-26 13:45:00