pessoa = {"nome": "Paulo", "idade": 28}
print(pessoa) # {'nome': 'Paulo', 'idade': 28}

pessoa = dict(nome = "Paulo", idade = 28)
print(pessoa) # {'nome': 'Paulo', 'idade': 28}

pessoa["telefone"] = "3333-1234"
print(pessoa) # {'nome': 'Paulo', 'idade': 28, 'telefone': '3333-1234'}