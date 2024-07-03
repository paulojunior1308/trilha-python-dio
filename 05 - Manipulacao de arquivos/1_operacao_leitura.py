arquivo = open("C:/Users/paulo.junior/OneDrive - SERVICO SOCIAL DO COMERCIO-SESC/Área de Trabalho/Aulas DIO/projetos-dio/Python/Trilha-Python-Dio/05 - Manipulacao de arquivos/lorem.txt", "r")
print(arquivo.read()) # Todo conteudo de uma vez
print(arquivo.readline()) # Linha por linha
print(arquivo.readlines()) # Todo conteudo em uma lista

# tip
#while len(linha := arquivo.readline()):
#    print(linha)

arquivo.close()




##### METODO READ #####
## Ler todo o conteudo do arquivo de uma vez
#file = open('example.txt', 'r')
#print(file.read())
#file.close()