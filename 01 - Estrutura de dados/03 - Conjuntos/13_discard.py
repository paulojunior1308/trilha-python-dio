numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.discard(1)
numeros.discard(45)
print(numeros) # {0, 2, 3, 4, 5, 6, 7, 8, 9}