contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-33333"},
    "paulo@gmail.com": {"nome": "Paulo", "telefone": "3333-4444"},
    "eduardo@gmail.com": {"nome": "Eduardo", "telefone": "4444-33333"},
    "junior@gmail.com": {"nome": "Junior", "telefone": "3333-1235"},
}

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)