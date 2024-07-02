class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[1, 2, 3]):
    print(i)






###### EXEMPLO DE ITERADOR PARA LEITURA DE ARQUIVOS #####
#class FileIterator:
#    def __init__(self, filename):
#        self.file = open(filename)
#
#    def __iter__(self):
#        return self
#    
#    def __next__(self):
#        line = self.file.readline()
#        if line != '':
#            return line
#        else:
#            self.file.close()
#            raise StopIteration
#        
## Uso do FileIterator
#for line in FileIterator('large_file.txt'): #caminho do arquivo
#    print(line)