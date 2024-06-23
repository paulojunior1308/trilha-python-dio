contatos = {
    "paulo@gmail.com": {"nome": "Paulo", "telefone": "3333-4444"}
}

contatos.update({"paulo@gmail.com": {"nome": "Paulo Jr"}})
print(contatos) # {'paulo@gmail.com': {'nome': 'Paulo Jr'}}

contatos.update({"junior@gmail.com": {"nome": "Junior", "telefone": "3333-1235"}})
print(contatos) # {'paulo@gmail.com': {'nome': 'Paulo Jr'}, 'junior@gmail.com': {'nome': 'Junior', 'telefone': '3333-1235'}}

