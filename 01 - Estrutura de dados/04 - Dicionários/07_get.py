contatos = {
    "paulo@gmail.com": {"nome": "Paulo", "telefone": "3333-4444"}
}

#print(contatos["chave"]) # KeyError

print(contatos.get("chave")) # None
print(contatos.get("chave", {})) # {}
print(contatos.get("paulo@gmail.com", {})) # {'nome': 'Paulo', 'telefone': '3333-4444'}