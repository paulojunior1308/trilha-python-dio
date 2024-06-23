contatos = {
    "paulo@gmail.com": {"nome": "Paulo", "telefone": "3333-4444"}
}

pop = contatos.pop("paulo@gmail.com", "não encontrou")

print(pop) # {'nome': 'Paulo', 'telefone': '3333-4444'}

pop = contatos.pop("paulo@gmail.com", {})

print(pop) # {}