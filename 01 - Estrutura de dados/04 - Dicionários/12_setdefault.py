contato = {'nome': 'Paulo', 'telefone': '1111-1111'}

contato.setdefault("nome", "Vanessa")
print(contato) # {'nome': 'Paulo', 'telefone': '1111-1111'}

contato.setdefault("idade", 28)
print(contato) # {'nome': 'Paulo', 'telefone': '1111-1111', 'idade': 28}