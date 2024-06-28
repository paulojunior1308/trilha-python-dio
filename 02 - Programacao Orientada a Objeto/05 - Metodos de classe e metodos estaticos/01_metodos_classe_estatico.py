class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

# p = Pessoa("Paulo", 28)
# print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nascimento(1996, 8, 13, "Paulo")
print(p2.nome, p2.idade)

print(Pessoa.maior_idade(28))