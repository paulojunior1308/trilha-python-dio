### FILTRO VERSÃO 1 ###

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(numero) 


### FILTRO VERSÃO 2 ###
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
       

### MODIFICANDO VALORES VERSÃO 1 ###
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    
print(quadrado)

 ### MODIFICANDO VALORES VERSÃO 2 ###
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]   
print(quadrado)