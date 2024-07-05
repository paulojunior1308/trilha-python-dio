import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(conexao, cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?;", data)
    conexao.commit()

def deletar_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id = ?;", data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()

def consultar_registro(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?;", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")



cliente = consultar_registro(cursor, 1)
print(dict(cliente))     

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

print(f"Seja bem vindo ao sistema {cliente["nome"]}")

# inserir_registro(conexao, cursor, "Vanessa Oliveira", "vanessa@vanessa.com")
# atualizar_registro(conexao, cursor, "Paulo Eduardo", "paulo@paulo.com", 1)
# deletar_registro(conexao, cursor, 2)

#dados = [
#    ("Paulo", "paulo@gmail.com"),
#    ("Eduardo", "eduardo@gmail.com"),
#    ("Junior", "junior@gmail.com"),
#]
#inserir_muitos(conexao, cursor, dados)