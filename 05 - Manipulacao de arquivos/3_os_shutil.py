import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent # Modo de trazer o caminho da pasta onde quer criar o arquivo ou outro diretório

# Criando uma pasta
os.mkdir(ROOT_PATH / "novo-diretorio")

# Criando um arquivo
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# Renomeando um arquivo
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# Removendo um arquivo
os.remove(ROOT_PATH / "alterado.txt")

# Movendo um arquivo
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")






##### EXEMPLO DE CÓDIGO #####
#import os
#import shutil
#
## Criar um diretório
#os.mkdir("exemplo")
#
## Renomear um arquivo
#os.rename("old.txt", "new.txt")
#
## Remover um arquivo
#os.remove("unwanted.txt")
#
## Mover um arquivo
#shutil.move("source.txt", "destination.txt")