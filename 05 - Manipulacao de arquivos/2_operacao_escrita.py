arquivo = open("C:/Users/paulo.junior/OneDrive - SERVICO SOCIAL DO COMERCIO-SESC/Área de Trabalho/Aulas DIO/projetos-dio/Python/Trilha-Python-Dio/05 - Manipulacao de arquivos/teste.txt", "w")

arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n","escrevendo","\n", "um","\n", "novo","\n", "texto"])

arquivo.close()





##### EXEMPLO DE CÓDIGO #####
#file = open('example.txt', 'w')
#file.write("Olá, mundo!")
#file.close()